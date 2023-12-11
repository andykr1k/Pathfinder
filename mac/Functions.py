def DetectObjects(current_node, tree):
    
    return

# Equation to use for distance to object

# Parameters(All in mm unless stated otherwise)

# focal_length: Raspberry Pi Camera V2
# sensor_height: Raspberry Pi Camera V2
# sensor_width: Raspberry Pi Camera V2
# object_height: Obstacle Height
# object_width: Obstacle Width
# object_height_pixels: Obstacle Height in pixels
# object_width_pixels: Obstacle Width in pixels
# image_height: Resolution of Frame
# image_width: Resolution of Frame

# distance = (focal_length * object_height * image_height) / (object_height_pixels * sensor_height)

# distance = (focal_length * object_width * image_width) / (object_width_pixels * sensor_width)

def GenerateDistance():
    focal_length = 0
    sensor_height = 0
    sensor_width = 0
    object_height = 0
    object_width = 0
    object_height_pixels = 0
    object_width_pixels = 0
    image_height = 0
    image_width = 0

    distance_height = (focal_length * object_height * image_height) / \
        (object_height_pixels * sensor_height)
    
    distance_width = (focal_length * object_width * image_width) / \
        (object_width_pixels * sensor_width)

    return distance_height, distance_width

def GenerateMovements(distance):
    return

def DriveToObject(node, direction):
    if direction == "forward":
        return
    elif direction == "backward":
        return
    return

def DriveToRoot(current_node, tree, stack):
    while (current_node != tree.root):
        next_node = stack.pop()
        DriveToObject(next, "backward")
        current_node = next_node
    return