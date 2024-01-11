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
    if type(boxes) is not list or not boxes:
        return False

    unlocked_boxes = [0]

    for n in unlocked_boxes:
        for k in boxes[n]:
            """ Update the status of the boxes that can be unlocked"""
            if k not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(k)

    if len(unlocked_boxes) == leb(boxes):
        return True
    return False
