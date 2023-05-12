#!/usr/bin/python3
"""Module for log passing."""
import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size = 0


def print_metric():
    """Print of the log."""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    count = 0
    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                file_size += int(parts[-1])
                if parts[-2] in status_codes:
                    status_codes[parts[-2]] += 1
            except Exception:
                pass
            if count == 9:
                print_metric()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_metric()
        raise
    print_metric()
