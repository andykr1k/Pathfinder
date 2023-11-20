import cv2
import numpy as np


def calculate_distance(image_path, left_point, right_point):
    # Read the image
    image = cv2.imread(image_path)

    # Assume you know the camera's focal length in pixels
    # For example, let's say the focal length is 1000 pixels
    focal_length_pixels = 1000.0

    # Assume you know the width of the sensor in millimeters
    # For example, let's say the sensor width is 10 mm
    sensor_width_mm = 10.0

    # Calculate the field of view (FOV) in radians
    fov_radians = 2 * np.arctan((sensor_width_mm / 2) / focal_length_pixels)

    # Calculate the distance between the left and right points in pixels
    pixel_distance = abs(right_point[0] - left_point[0])

    # Calculate the estimated distance to the dots in millimeters
    distance_mm = (focal_length_pixels * sensor_width_mm) / \
        (2 * pixel_distance * np.tan(fov_radians / 2))

    return distance_mm

def find_and_draw_boundary(image_path, target_color):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB color space
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the lower and upper bounds for the target color in HSV
    lower_bound = np.array(
        [target_color[0] - 28, target_color[1] - 28, target_color[2] - 28])
    upper_bound = np.array(
        [target_color[0] + 28, target_color[1] + 28, target_color[2] + 28])

    # Create a mask using the inRange function
    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key=cv2.contourArea)

    # Draw a red boundary around the largest box
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Calculate the midpoints of the left and right edges
    left_midpoint = (x, y + h // 2)
    right_midpoint = (x + w, y + h // 2)

    # Draw dots on the midpoints
    # Blue dot for left edge
    cv2.circle(image, left_midpoint, 5, (255, 0, 0), -1)
    # Green dot for right edge
    cv2.circle(image, right_midpoint, 5, (0, 255, 0), -1)

    distance = calculate_distance(image_path, left_midpoint, right_midpoint)
    print(f"Estimated distance between dots: {distance:.2f} cm")

    # Display the result
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'assets/box.jpeg'
target_color = (200, 160, 120)  # Target color in RGB

find_and_draw_boundary(image_path, target_color)
