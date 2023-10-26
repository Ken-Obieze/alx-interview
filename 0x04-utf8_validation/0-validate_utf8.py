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
    remaining_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if remaining_bytes == 0:
            if byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

            remaining_bytes -= 1

    return remaining_bytes == 0
