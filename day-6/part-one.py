import sys
from pathlib import Path

file = "test" if sys.argv[-1] == "-t" else "input"
path = Path(__file__).parent / f"{file}.txt"

with open(path, "r") as f:
    input = f.read()

input = input.splitlines()

rows = [line.split() for line in input]
values = [[int(value) for value in row] for row in rows[:-1]]
operators = rows[-1:][0]

row_len = len(values)
column_len = len(values[0])
grand_total = 0

for j in range(column_len):
    local_total = values[0][j]

    for i in range(1, row_len):
        if operators[j] == "+":
            local_total += values[i][j]
        else:
            local_total *= values[i][j]

    grand_total += local_total

print("global total:", grand_total)
