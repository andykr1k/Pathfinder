import cv2
import numpy as np


def find_and_draw_boundary(image_path, target_color):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB color space
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the lower and upper bounds for the target color in HSV
    padding = 50
    lower_bound = np.array(
        [target_color[0] - padding, target_color[1] - padding, target_color[2] - padding])
    upper_bound = np.array(
        [target_color[0] + padding, target_color[1] + padding, target_color[2] + padding])

    # Create a mask using the inRange function
    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key=cv2.contourArea)

    # Draw a red boundary around the largest box
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    car_offset = 50

    # Calculate the midpoints of the left and right edges
    left_midpoint = (x - car_offset, y + h // 2)
    right_midpoint = (x + w + car_offset, y + h // 2)

    # Draw dots on the midpoints
    # Blue dot for left edge
    cv2.circle(image, left_midpoint, 5, (255, 0, 0), -1)
    # Green dot for right edge
    cv2.circle(image, right_midpoint, 5, (0, 255, 0), -1)

    focal_length = 3.04
    sensor_width = 3.674
    # Assuming a fixed camera orientation and no tilt or rotation
    # Angle from camera to blue dot (left midpoint)
    angle_blue = np.arctan(
        (left_midpoint[0] - image.shape[1] / 2) / focal_length)
    angle_blue_deg = np.degrees(angle_blue)

    # Angle from camera to green dot (right midpoint)
    angle_green = np.arctan(
        (right_midpoint[0] - image.shape[1] / 2) / focal_length)
    angle_green_deg = np.degrees(angle_green)

    # Calculate distances from camera to dots using similar triangles
    # Correcting the distance calculation for blue and green dots
    distance_blue_mm = (sensor_width * focal_length) / \
        (2 * np.tan(angle_blue / 2))
    distance_green_mm = (sensor_width * focal_length) / \
        (2 * np.tan(angle_green / 2))

    # Draw the angles as text on the image
    scale = 0.5
    text_position_blue = (200, 40)
    text_position_green = (200, 60)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Put the angle text and distance text at the specified positions
    cv2.putText(image, f'Angle to Blue: {angle_blue_deg:.2f} degrees, Distance: {distance_blue_mm:.2f} mm',
                text_position_blue, font, scale, (0, 0, 0), 1)
    cv2.putText(image, f'Angle to Green: {angle_green_deg:.2f} degrees, Distance: {distance_green_mm:.2f} mm',
                text_position_green, font, scale, (0, 0, 0), 1)

    # Display the result
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = 'mac/assets/redbox.png'
target_color = (220, 0, 40)  # Target color in RGB

find_and_draw_boundary(image_path, target_color)
