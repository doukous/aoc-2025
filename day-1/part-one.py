import sys
from pathlib import Path

file = "test" if sys.argv[-1] == "-t" else "input"
path = Path(__file__).parent / f"{file}.txt"

with open(path, "r") as f:
    input = f.read()

input = input.splitlines()
turns = [(line[:1], int(line[1:])) for line in input]

password = 0
distance = 50

for turn in turns:
    if turn[0] == "R":
        distance += turn[1]
    else:
        distance -= turn[1]

    distance %= 100
    if not distance:
        password += 1

print("distance:", distance, "\npassword :", password)
