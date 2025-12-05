import sys
from pathlib import Path

file = "test" if sys.argv[-1] == "-t" else "input"
path = Path(__file__).parent / f"{file}.txt"

with open(path, "r") as f:
    input = f.read()

input = input.splitlines()
table = [[position for position in row] for row in input]

row_len = len(table)
column_len = len(table[0])

accessed_rolls = 0


def print_overview():
    print("total of rolls:", accessed_rolls, "\n")

    for row in table:
        print(row)


for ridx in range(row_len):
    for cidx in range(column_len):
        adjacent_rolls = 0

        if table[ridx][cidx] == "@":
            if cidx - 1 >= 0 and table[ridx][cidx - 1] in ["@", "x"]:
                adjacent_rolls += 1

            if cidx + 1 < column_len and table[ridx][cidx + 1] in ["@", "x"]:
                adjacent_rolls += 1

            if ridx - 1 >= 0 and table[ridx - 1][cidx] in ["@", "x"]:
                adjacent_rolls += 1

            if ridx + 1 < row_len and table[ridx + 1][cidx] in ["@", "x"]:
                adjacent_rolls += 1

            if (
                cidx - 1 >= 0
                and ridx - 1 >= 0
                and table[ridx - 1][cidx - 1] in ["@", "x"]
            ):
                adjacent_rolls += 1

            if (
                cidx + 1 < column_len
                and ridx - 1 >= 0
                and table[ridx - 1][cidx + 1] in ["@", "x"]
            ):
                adjacent_rolls += 1

            if (
                cidx - 1 >= 0
                and ridx + 1 < row_len
                and table[ridx + 1][cidx - 1] in ["@", "x"]
            ):
                adjacent_rolls += 1

            if (
                cidx + 1 < column_len
                and ridx + 1 < row_len
                and table[ridx + 1][cidx + 1] in ["@", "x"]
            ):
                adjacent_rolls += 1

            if adjacent_rolls < 4:
                accessed_rolls += 1
                table[ridx][cidx] = "x"


# print_overview()
