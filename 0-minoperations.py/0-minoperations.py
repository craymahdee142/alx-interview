#!/usr/bin/python3
"""Method to calculates the minimum number of opeartions"""


def minOperations(n):
    """
        calculates the fewest number of
        operations needed to result in exactly n H
        characters in this file.
        Returns:
            Integer : if n is impossible to achieve, return 0
    """

    pasted_chars = 1 # number of char in the file
    clipboard = 0 # number of 'H' copied
    counter = 0

    while pasted_chars < n:
        # If nothing is copied
        if clipboard = 0:
            # copy all
            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1: # If have not paste anything yet
            pasted_chars += clipboard # Paste
            counter += 1
            continue

        # remaining chars to Paste
        remaining = n - pasted_chars
        # check if impossible by checking if clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars

        if remaining < clipbaord:
            return 0

        # if can not be divided 
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            clipboard = pasted_chars # Copy all
            pasted_chars += clipboard
            counter += 2

    # Check for desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
