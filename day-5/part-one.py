import sys
from pathlib import Path

file = "test" if sys.argv[-1] == "-t" else "input"
path = Path(__file__).parent / f"{file}.txt"

with open(path, "r") as f:
    input = f.read()

input = input.splitlines()

separator_line_index = 0

for i, el in enumerate(input):
    if not el:
        separator_line_index = i

fresh_inredients = [str_range.split("-") for str_range in input[:separator_line_index]]
fresh_inredients_ranges = [(int(start), int(end)) for start, end in fresh_inredients]
available_ingredients = [int(i) for i in input[separator_line_index + 1 :]]

number_of_available = 0

for id in available_ingredients:
    for start, end in fresh_inredients_ranges:
        if id >= start and id <= end:
            number_of_available += 1
            break

print("number of available:", number_of_available)
