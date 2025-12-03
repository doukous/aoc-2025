import sys
from pathlib import Path

file = "test" if sys.argv[-1] == "-t" else "input"
path = Path(__file__).parent / f"{file}.txt"

with open(path, "r") as f:
    input = f.read()

batteries = input.splitlines()

banks_list = [
    [int(battery[joltage_index]) for joltage_index in range(len(battery))]
    for battery in batteries
]

total_voltage = 0

for bank in banks_list:
    highest_first_value = max(bank[:-1])
    index_first_max = bank.index(highest_first_value)

    second_value = max(bank[index_first_max + 1 :])
    final_value = int("".join([str(highest_first_value), str(second_value)]))

    total_voltage += final_value
    print(final_value)


print("\ntotal output joltage:", total_voltage)
