#!/usr/bin/python3
"""
This module defines the function canUnlockAll
which determines if all boxes in a list can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of list): A list where each inner list contains keys for other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
n = len(boxes)  # Number of boxes
opened_boxes = [False] * n  # Track which boxes are opened, initially none are
opened_boxes[0] = True  # The first box is already unlocked
stack = [0]  # Start with the first box

while stack:
current_box = stack.pop()  # Take a box from the stack
for key in boxes[current_box]:  # Look at the keys in this box
if key < n and not opened_boxes[key]:  # Check if the key is valid and if the box is not already opened
opened_boxes[key] = True  # Mark this box as opened
stack.append(key)  # Add this box to the stack to explore its keys
return all(opened_boxes)  # Check if all boxes are opened
