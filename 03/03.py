from collections import defaultdict
from copy import deepcopy

with open("03.in", "r") as f:
    # with open("03-test.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n")]
# print(nr_list)

dict = defaultdict(list)

for i in nr_list:
    for j in range(len(i)):
        dict[j].append(i[j])


gamma = ""

for a, b in dict.items():
    gamma += max(b, key=b.count)

# print(gamma)
# print(int(gamma, 2))

epsilon = "".join([("0" if x == "1" else "1") for x in gamma])

# print(epsilon)
# print(int(epsilon, 2))

print(f"Part 1: {int(gamma,2)*int(epsilon,2)}")

# Part 2
o = deepcopy(nr_list)
co = deepcopy(nr_list)
binlen = len(nr_list[0])

for i in range(binlen):
    one = []
    zero = []
    for j in o:
        one.append(j) if j[i] == "1" else zero.append(j)
    if len(one) >= len(zero):
        o = deepcopy(one)
    else:
        o = deepcopy(zero)
    if len(o) == 1:
        break

# print(o)

for i in range(binlen):
    one = []
    zero = []
    for j in co:
        one.append(j) if j[i] == "1" else zero.append(j)
    if len(zero) <= len(one):
        co = deepcopy(zero)
    else:
        co = deepcopy(one)
    # print(f"Bit {i}, one={one}, zero={zero}, CO={co}")
    if len(co) == 1:
        break

# print(co)

print(f"Part 2: {int(o[0], 2)*int(co[0], 2)}")
