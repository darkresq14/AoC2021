# How many are bigger than the previous

import itertools


def bigger_than_previous(a, b):
    # print(a, b)
    return b > a


with open("01.in", "r") as f:
    raw = f.read()

nr_list = [int(x) for x in raw.split("\n")]
previous = "test"
result = 0

# First Part
for num in nr_list:
    if previous == "test":
        previous = num
        continue
    if bigger_than_previous(previous, num):
        result += 1
    previous = num

# Second Part
pos = 0
condition = True
count = 0

while condition:
    one = nr_list[pos]
    two = nr_list[pos + 1]
    three = nr_list[pos + 2]
    four = nr_list[pos + 3]
    first = one + two + three
    second = two + three + four
    if bigger_than_previous(first, second):
        count += 1
    pos += 1
    if pos + 3 >= len(nr_list):
        condition = False


print(f"First part: {result}")
print(f"Second part: {count}")
