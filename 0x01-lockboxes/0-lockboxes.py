#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUlockedAll(boxes):
    """
    Function that check if all boxes can be opened
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    unlocked_boxes[0] = True
    """ Check for total number of boxes"""
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes

    for k in range(num_boxes):
        for i in boxes[i]:
            """ Update the status of the boxes that can be unlocked"""
            if 0 <= i < num_boxes:
                unlocked_boxes[i] = True
    return all(unlockde_boxes)
