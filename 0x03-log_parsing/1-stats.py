#!/usr/bin/python3

import sys
import signal

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_dict = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print(f"Total file size: {total_size}")
    for code in sorted(status_dict.keys()):
        if status_dict[code] > 0:
            print(f"{code}: {status_dict[code]}")

signal.signal(signal.SIGINT, signal_handler)

def main():
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue
        ip, date, method, path, protocol, status, size = parts
        try:
            size = int(size)
            status = int(status)
        except ValueError:
            continue
        if status not in status_codes:
            continue
        status_dict[status] += 1
        total_size += size
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

if __name__ == "__main__":
    main()

