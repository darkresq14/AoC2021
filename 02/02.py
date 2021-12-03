with open("02.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n")]

hor = 0
ver = 0

# Part 1
for i in nr_list:
    dir, nr = i.split(" ")
    if dir == "forward":
        hor += int(nr)
    elif dir == "up":
        ver -= int(nr)
    elif dir == "down":
        ver += int(nr)

print(f"Part 1: {hor*ver}")

# Part 2
aim = 0
hor = 0
ver = 0

for i in nr_list:
    dir, nr = i.split(" ")
    nr = int(nr)
    if dir == "forward":
        hor += nr
        ver += aim * nr
    elif dir == "up":
        aim -= nr
    elif dir == "down":
        aim += nr

print(f"Part 2: {hor*ver}")

# print(nr_list)
