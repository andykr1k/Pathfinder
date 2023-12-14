import cv2
import numpy as np
from motor import *

def calculate_distances(left_midpoint, right_midpoint, frame):
    focal_length = 3.04
    sensor_width = 3.67

    # Calculate distances from camera to dots using similar triangles
    distance_left_mm = (sensor_width * focal_length) / \
        (2 * np.tan(np.arctan((left_midpoint[0] -
         frame.shape[1] / 2) / focal_length) / 2))
    distance_right_mm = (sensor_width * focal_length) / \
        (2 * np.tan(np.arctan((right_midpoint[0] -
         frame.shape[1] / 2) / focal_length) / 2))

    return distance_left_mm, distance_right_mm


def drive_towards_largest_box(largest_contours, frame, car_offset, distance_left_mm, distance_right_mm):
    if not largest_contours:
        # No largest box found, stop or take appropriate action
        print("No largest box found.")
        return

    # Get the largest box
    largest_box_contour = largest_contours[0]
    x, y, w, h = cv2.boundingRect(largest_box_contour)
    print("Largest Box X:" + str(x))
    print("Largest Box Y:" + str(y))
    # Check if the box is centered horizontally
    center_threshold = 10  # Adjust as needed
    if abs(x + w // 2 - frame.shape[1] // 2) > center_threshold:
        while abs(x + w // 2 - frame.shape[1] // 2) > center_threshold:
            if x + w // 2 - frame.shape[1] // 2 > 0:
                driveLeft()
            else:
                driveRight()
        TurnOffPins()
        print(f"Adjusting to center.")
    else:
        driveForward()
        print(
            f"Driving towards the largest box.")


def find_and_draw_boundary(target_color):
    # Open a video capture object (0 is usually the default webcam)
    cap = cv2.VideoCapture(0)
    
    start = input("Start or Test?")

    while start == "Start":
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Flip the frame vertically
        frame = cv2.flip(frame, 0)

        # Convert the frame from BGR to RGB color space
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Define the lower and upper bounds for the target color in HSV
        padding = 10
        lower_bound = np.array(
            [target_color[0] - padding*4, target_color[1] - padding*2, target_color[2] - padding*2])
        upper_bound = np.array(
            [target_color[0] + padding*10, target_color[1] + padding*2, target_color[2] + padding*2])

        # Create a mask using the inRange function
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # Find contours in the mask
        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # largest_contours = []

        # for contour in contours:
        #     contour_area = cv2.contourArea(contour)
        #     if contour_area > 500:
        #         largest_contours.append(contour)
        #         max_contour_area = contour_area

        # Calculate areas of contours
        areas = [cv2.contourArea(contour) for contour in contours]

        # Combine contours and areas into a list of tuples (contour, area)
        contours_with_areas = list(zip(contours, areas))

        # Sort the list of contours based on areas in descending order (largest to smallest)
        sorted_contours = sorted(contours_with_areas, key=lambda x: x[1], reverse=True)

        # Extract sorted contours without areas
        largest_contours = [contour for contour, _ in sorted_contours]

        for contour in largest_contours:

            # Draw a red boundary around the largest box
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            car_offset = 50

            # Calculate the midpoints of the left and right edges
            left_midpoint = (x - car_offset, y + h // 2)
            right_midpoint = (x + w + car_offset, y + h // 2)

            # Draw dots on the midpoints
            # Blue dot for left edge
            cv2.circle(frame, left_midpoint, 5, (255, 0, 0), -1)
            # Green dot for right edge
            cv2.circle(frame, right_midpoint, 5, (0, 255, 0), -1)
            
            # Calculate distances from camera to dots using similar triangles
            distance_left_mm, distance_right_mm = calculate_distances(
                left_midpoint, right_midpoint, frame)

            title = f'Box {largest_contours.index(contour) + 1} - Left: {distance_left_mm:.2f} mm, Right: {distance_right_mm:.2f} mm'
            title_position = (x + w // 2, y - 10)  # Adjust the vertical offset as needed
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            cv2.putText(frame, title, title_position, font, font_scale, (0, 255, 0), font_thickness)

            drive_towards_largest_box(largest_contours, frame, car_offset, distance_left_mm, distance_right_mm)

            # Assuming a fixed camera orientation and no tilt or rotation
            # Angle from camera to blue dot (left midpoint)
            # angle_blue = np.arctan(
            #     (left_midpoint[0] - frame.shape[1] / 2) / focal_length)
            # angle_blue_deg = np.degrees(angle_blue)

            # Angle from camera to green dot (right midpoint)
            # angle_green = np.arctan(
            #     (right_midpoint[0] - frame.shape[1] / 2) / focal_length)
            # angle_green_deg = np.degrees(angle_green)

            # Calculate distances from camera to dots using similar triangles
            # Correcting the distance calculation for blue and green dots
            # distance_blue_mm = (sensor_width * focal_length) / \
            #     (2 * np.tan(angle_blue / 2))
            # distance_green_mm = (sensor_width * focal_length) / \
            #     (2 * np.tan(angle_green / 2))

            # Draw the angles as text on the frame
            # scale = 0.5
            # text_position_blue = (200, 40)
            # text_position_green = (200, 60)
            # font = cv2.FONT_HERSHEY_SIMPLEX

            # # Put the angle text and distance text at the specified positions
            # cv2.putText(frame, f'Angle to Blue: {angle_blue_deg:.2f} degrees, Distance: {distance_blue_mm:.2f} mm',
            #             text_position_blue, font, scale, (0, 0, 0), 1)
            # cv2.putText(frame, f'Angle to Green: {angle_green_deg:.2f} degrees, Distance: {distance_green_mm:.2f} mm',
            #             text_position_green, font, scale, (0, 0, 0), 1)

        # Display the result
        cv2.imshow('Result', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    TurnOffPins()
    clean()
    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
target_color = (90, 0, 20)  # Target color in RGB
find_and_draw_boundary(target_color)