from tests.Test import TestAlgos
from functions.camera import find_and_draw_boundary

def main():
    # TestAlgos()

    # algorithms = ["DFS", "BFS"]
    # title = 'Which algorithm would you like to use: '
    # option, index = pick(algorithms, title)

    # print("Selected algorithm: " + algorithms[index])

    # Test - Object Detection - See Objects - Check
    # Test - Movement Generator - Move to Objects
    find_and_draw_boundary()
    # Test - Decision Maker - Move around objects
    # Test - Target Function - Move to Target Node
    return

if __name__ == '__main__':
    main()

# Routine

# 1) Place pathfinder at start of maze
# 2) Choose search algorithm
# 3) Press "Start"
# 4) Complete Maze
# 5) Restart from 2

# Main Loop

# 1) Create tree with root node as starting position as well as a stack with recently visited node
# 2) Look for target if found add paths to tree with generated movements to target and drive to target
# 3) Look for obstacles if founde add paths to tree with generated movements
# 4) Drive to next node depending on search algo
# 5) Repeat from 2
# 6) Drive back to root using generated movements
# 7) Restart

# Expanded Loop

# 1) Create tree with root node as starting position

# Create root
# Create tree

# 2) Look for target if found add paths to tree with generated movements to target and drive to target

# Open camera
# Detect target
# Generate distance to target
# Use distance to generate movements to target
# Add path to tree with generated movements and distance marked as target node
# Using target node movements drive to target node
# Add current node to stack
# Set current node to target node

# 3) Look for obstacles if found add paths to tree with generated movements

# Open camera
# Detect obstacles
# Generate distance to obstacles
# Use distance to generate movements to obstacles
# Add path to tree with generated movements and distance marked as obstacle node

# 4) Drive to next node depending on search algo

# Select next obstacle node to explore using said search algo
# Drive to next obstacle node
# Add current node to stack
# Set current position to next node

# 5) Repeat from 2

# Loop will be broken once target is found

# 6) Drive back to root using generated movements

# Pop Stack
# Use backward movement
# Repeat until start node is reached

# 7) Restart

# Back to search algorithm selection