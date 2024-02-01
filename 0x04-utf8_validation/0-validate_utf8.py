#!/usr/bin/python3

"""UTF-8 Validation"""


def validUTF8(data):
    """
    data: list of integers
    Return: True if data is valid UTF-8
    encoding, else False
    """
    byte_count = 0

    for i in data:
        """Check if the integers is within the valid byte range"""
        if i < 0 or i > 255:
            return False

        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count == 1
            elif i >> 4 == 0b1110:
                byte_count == 2
            elif i >> 3 == 0b11110:
                byte_count == 3
            elif 1 >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
