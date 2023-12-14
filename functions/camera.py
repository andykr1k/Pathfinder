import cv2
import numpy as np
from time import sleep
from functions.motor import *

def drive_towards_target(target_contour, frame, car_offset):
    if not target_contour:
        print("No target found.")
        return

    x, y, w, h = cv2.boundingRect(target_contour[0])
    area = cv2.contourArea(target_contour[0])
    print("Target Midpoint:" + str(x + w // 2 - frame.shape[1] // 2))
    print("Area of Target:" + str(area))
    # Check if the box is centered horizontally
    center_threshold = 25  # Adjust as needed
    norm_x = x + w // 2 - frame.shape[1] // 2
    if abs(norm_x) > center_threshold:
        if norm_x > center_threshold:
            print("Driving Left")
            driveLeft(abs(norm_x))
        elif norm_x < -1*center_threshold:
            print("Driving Right")
            driveRight(abs(norm_x))
        TurnOffPins()
        print(f"Adjusting to center.")
    else:
        driveForward(area)
        print(f"Driving towards the target.")
    return

def drive_around_box():
    # Depends on search algo
    print("Driving Around Largest Box")
    driveRight(175)
    driveForward(5000)
    driveLeft(175)

def drive_towards_largest_box(largest_contours, frame, car_offset):
    if not largest_contours:
        # No largest box found, stop or take appropriate action
        print("No largest box found.")
        return

    # Get the largest box
    largest_box_contour = largest_contours[0]
    x, y, w, h = cv2.boundingRect(largest_box_contour)
    area = cv2.contourArea(largest_box_contour)
    print("Largest Box Midpoint:" + str(x + w // 2 - frame.shape[1] // 2))
    print("Area of Box:" + str(area))
    # Check if the box is centered horizontally
    center_threshold = 25  # Adjust as needed
    norm_x = x + w // 2 - frame.shape[1] // 2
    if abs(norm_x) > center_threshold:
        if norm_x > center_threshold:
            print("Driving Left")
            driveLeft(abs(norm_x))
        elif norm_x < -1*center_threshold:
            print("Driving Right")
            driveRight(abs(norm_x))
        TurnOffPins()
        print(f"Adjusting to center.")
    else:
        if area > 35000:
            drive_around_box()
        else:
            driveForward(area)

        print(f"Driving towards the largest box.")
    return

def find_and_draw_boundary():
    cap = cv2.VideoCapture(0)
    frame_counter = 0
    start = input('Start or Quit?\n')
    
    while start == "s":
        # Read a frame from the webcam
        ret, frame = cap.read()
        car_offset = 50

        # Flip the frame vertically
        frame = cv2.flip(frame, 0)
        frame_counter+=1

        # Convert the frame from BGR to RGB color space
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Define the lower and upper bounds for the target color in RGB
        lower_bound_objects = np.array([75, 0, 0])
        upper_bound_objects = np.array([255, 50, 50])
        lower_bound_target = np.array([75, 75, 30])
        upper_bound_target = np.array([125, 125, 70])

        # Create a mask using the inRange function
        mask_objects = cv2.inRange(
            frame_rgb, lower_bound_objects, upper_bound_objects)
        mask_target = cv2.inRange(
            frame_rgb, lower_bound_target, upper_bound_target)

        # Find contours in the mask
        contours, _ = cv2.findContours(
            mask_objects, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        contours_target, _ = cv2.findContours(
            mask_target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        largest_contours = []

        for contour in contours:
            contour_area = cv2.contourArea(contour)
            x,y,w,h = cv2.boundingRect(contour)
            if contour_area > 500 and h > 50:
                largest_contours.append(contour)
                

        largest_contours = sorted(largest_contours, key=lambda x: cv2.contourArea(x), reverse=True)

        largest_contours_target = []

        for contour in contours_target:
            contour_area = cv2.contourArea(contour)
            x,y,w,h = cv2.boundingRect(contour)
            if contour_area > 500 and h > 75:
                largest_contours_target.append(contour)

        largest_contours_target = sorted(
            largest_contours_target, key=lambda x: cv2.contourArea(x), reverse=True)

        for contour in largest_contours:

            # Draw a red boundary around the largest box
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Calculate the midpoints of the left and right edges
            left_midpoint = (x - car_offset, y + h // 2)
            right_midpoint = (x + w + car_offset, y + h // 2)
            midpoint = (x + w // 2, y + h // 2)
            # Draw dots on the midpoints
            # Blue dot for left edge
            cv2.circle(frame, left_midpoint, 5, (255, 0, 0), -1)
            # Green dot for right edge
            cv2.circle(frame, right_midpoint, 5, (0, 255, 0), -1)
            # Purple for for center 
            cv2.circle(frame, midpoint, 5, (150, 0, 150), -1)

            # title = f'Box {largest_contours.index(contour) + 1} - Left: {distance_left_mm:.2f} mm, Right: {distance_right_mm:.2f} mm'
            title = f'Obstacle'
            title_position = (x + w // 2, y - 10)  # Adjust the vertical offset as needed
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            cv2.putText(frame, title, title_position, font, font_scale, (0, 255, 0), font_thickness)

        if largest_contours_target != []:

            # Draw a red boundary around the largest box
            x, y, w, h = cv2.boundingRect(largest_contours_target[0])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Calculate the midpoints of the left and right edges
            midpoint_target = (x + w // 2, y + h // 2)
            # Draw dots on the midpoints
            # Purple for for center
            cv2.circle(frame, midpoint_target, 5, (150, 0, 150), -1)

            title = f'Target'
            # Adjust the vertical offset as needed
            title_position = (x + w // 2, y - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            cv2.putText(frame, title, title_position, font,
                        font_scale, (0, 255, 0), font_thickness)
            
        # Display the result
        cv2.imshow('Result', frame)

        if frame_counter % 20 == 0:
            if largest_contours_target == []:
                if largest_contours != []:
                    drive_towards_largest_box(largest_contours, frame, car_offset)
                else:
                    print("Field is Empty!")
            else:
                drive_towards_target(largest_contours_target, frame, car_offset)

        # Break the loop if 'q' is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        sleep(0.25)

    TurnOffPins()
    clean()
    cap.release()
    cv2.destroyAllWindows()
