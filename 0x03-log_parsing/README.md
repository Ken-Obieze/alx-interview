# Log File Metrics

This Python script reads log entries from standard input and computes metrics. It prints the following statistics every 10 lines or keyboard interruption:

- Total file size: the sum of all previous file sizes
- Number of lines by status code: the count of log entries for each HTTP status code that appears at least once

## Input Format

The script expects input log entries in the following format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> 


If an input line doesn't match this format, it will be skipped.

## Output Format

The script prints statistics every 10 lines or keyboard interruption in the following format:

Total file size: <total size>
<status code>: <number>


The `<total size>` is the sum of all previous file sizes, and the `<status code>` and `<number>` represent the HTTP status code and the count of log entries for that status code, respectively.

Status codes are printed in ascending order.

## Usage

To run the script, pipe your log file or input into the script:

```sh
./0-generator.py | ./0-stats.py

Or you can run the script and enter your input manually:
python3 0-stats.py

Press CTRL + C to interrupt the script and print the current statistics.
