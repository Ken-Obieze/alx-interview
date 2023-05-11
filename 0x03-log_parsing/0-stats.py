#!/usr/bin/python3
"""Module for log passing."""
import random
import sys
from time import sleep
import datetime


try:
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    for line in sys.stdin:
        try:
            ip_address, _, _, _, status_code_str, file_size_str = line.split()[0:5]
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except (ValueError, IndexError):
            continue

        total_size += file_size
        status_codes[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    print(f"\nTotal file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    print()
