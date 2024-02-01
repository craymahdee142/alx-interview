#!/usr/bin/python3

"""UTF-8 Validation"""


def validUTF8(data):
    """
    data: list of integers
    Return: True if data is valid UTF-8
    encoding, else False
    """
    byte_count = 0

    # Mask to check the bits of each byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:
        """Check if the integers is within the valid byte range"""
        i = i & 255
        if byte_count == 0:
            # Determine the number of bytes in the uTF-8
            mask = 1 << 7
            while mask & i:
                byte_count += 1
                mask >>= 1

            # If it's a single byte character
            if byte_count == 0:
                continue

            # UTF-8 charac can be 1 or 4 long
            if byte_count == 1 or byte_count > 4:
                return False

            byte_count -= 1

        else:
            if not (i & mask1 and not (i & mask2)):
                return False
            byte_count -= 1

    return byte_count == 0
