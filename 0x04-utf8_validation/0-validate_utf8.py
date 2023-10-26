#!/usr/bin/python3
"""UTF8 validation Module."""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    consecutive_ones = 0

    for byte in data:
        if byte < 256:
            if consecutive_ones == 0:
                if (byte >> 7) & 1 == 0:
                    continue
                elif (byte >> 6) & 3 == 2:
                    return False
                consecutive_ones = 1
            else:
                if (byte >> 6) & 3 == 2:
                    consecutive_ones -= 1
                else:
                    return False
        else:
            return False
    return consecutive_ones == 0
