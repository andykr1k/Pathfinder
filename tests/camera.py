import cv2
import numpy as np
from time import sleep


def find_largest_contours(mask, min_area=500, min_height=50):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contours = []
    for contour in contours:
        contour_area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if contour_area > min_area and h > min_height:
            largest_contours.append(contour)
    largest_contours = sorted(
        largest_contours, key=lambda x: cv2.contourArea(x), reverse=True)
    return largest_contours


def find_and_draw_boundary():
    cap = cv2.VideoCapture(0)
    car_offset = 50
    frame_counter = 0
    while True:
        frame_counter += 1
        ret, frame = cap.read()
        frame = cv2.flip(frame, 0)
        frame = cv2.flip(frame, 1)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        lower_bound_objects = np.array([75, 0, 0])
        upper_bound_objects = np.array([255, 50, 50])
        lower_bound_target = np.array([75, 75, 30])
        upper_bound_target = np.array([125, 125, 60])

        mask_objects = cv2.inRange(
            frame_rgb, lower_bound_objects, upper_bound_objects)
        mask_target = cv2.inRange(
            frame_rgb, lower_bound_target, upper_bound_target)

        largest_contours_objects = find_largest_contours(mask_objects)
        largest_contours_target = find_largest_contours(mask_target)

        for contour in largest_contours_objects:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            left_midpoint = (x - car_offset, y + h // 2)
            right_midpoint = (x + w + car_offset, y + h // 2)
            midpoint = (x + w // 2, y + h // 2)

            cv2.circle(frame, left_midpoint, 5, (255, 0, 0), -1)
            cv2.circle(frame, right_midpoint, 5, (0, 255, 0), -1)
            cv2.circle(frame, midpoint, 5, (150, 0, 150), -1)

            title = f'Obstacle'
            title_position = (x + w // 2, y - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            cv2.putText(frame, title, title_position, font,
                        font_scale, (0, 255, 0), font_thickness)

        if largest_contours_target:
            x, y, w, h = cv2.boundingRect(largest_contours_target[0])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            midpoint_target = (x + w // 2, y + h // 2)
            cv2.circle(frame, midpoint_target, 5, (150, 0, 150), -1)

            title = f'Target'
            title_position = (x + w // 2, y - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            cv2.putText(frame, title, title_position, font,
                        font_scale, (0, 255, 0), font_thickness)

        cv2.imshow('Result', frame)

        if frame_counter % 15 == 0:
            if largest_contours_objects != []:
                if largest_contours_target != []:
                    if cv2.contourArea(largest_contours_objects[0])/2 > cv2.contourArea(largest_contours_target[0]):
                        print("Drive Towards Largest Box - Obstacle")
                    else:
                        print("Drive Toward Box - Target")
                else:
                    print("Drive Towards Largest Box - Obstacle")
            else:
                if largest_contours_target != []:
                        print("Drive Toward Box - Target")
                else:
                    print("Field is Empty!")

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        sleep(0.25)

    cap.release()
    cv2.destroyAllWindows()


find_and_draw_boundary()
