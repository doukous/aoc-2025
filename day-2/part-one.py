import sys
from pathlib import Path

file = "test" if sys.argv.count("-t") else "input"
path = Path(__file__).parent / f"{file}.txt"

with open(path, "r") as f:
    input = f.read()

input = input.split(",")
indexes = [index.split("-") for index in input]

ranges = [(int(index[0]), int(index[1])) for index in indexes]

sum = 0

for start, end in ranges:
    values = [value for value in range(start, end + 1)]

    for value in values:
        str_value = str(value)
        digits_num = len(str_value)

        if digits_num % 2 != 0:
            continue

        if str_value[: digits_num // 2] == str_value[digits_num // 2 :]:
            print(
                "str:",
                str_value,
                "| fh:",
                str_value[: digits_num // 2],
                "| sh:",
                str_value[digits_num // 2 :],
            )

            sum += value

print("\ntotal:", sum)
