from collections import Counter
from copy import deepcopy

with open("06/06.in", "r") as f:
    # with open("06/06-test.in", "r") as f:
    raw = f.read()

nr_list = [int(x) for x in raw.split(",")]


def part1(fishy, days):
    # print(f"Initial state: {fishy}")

    for i in range(1, days + 1):
        counter = 0
        length = len(fishy)

        while counter < length:
            if fishy[counter] == 0:
                fishy[counter] = 6
                fishy.append(8)
            else:
                fishy[counter] -= 1

            counter += 1

        # print(f"After {i} days: {fishy}")

    return fishy


# Part 2 copied from https://dev.to/qviper/advent-of-code-python-solution-day-6-22hl
# Was running forever without this optimisation


def part2(fishy, days):
    for day in range(1, days + 1):
        fishy = {
            l: (0 if fishy.get(l + 1) is None else fishy.get(l + 1))
            for l in range(-1, 8)
        }
        # make all 8s -1 because we create new fish with 8 after it reaches 0
        fishy[8] = fishy[-1]
        # add new fishy to that are exhausted
        fishy[6] += fishy[-1]
        # reset exhausted fishy
        fishy[-1] = 0

    return fishy


part1fishes = deepcopy(nr_list)

# Part 2 fishes to dict
part2fishes = dict(Counter(nr_list))

print(f"Part 1: {len(part1(part1fishes, 80))}")

print(f"Part 2: {sum(part2(part2fishes, 256).values())}")
