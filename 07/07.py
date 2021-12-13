with open("07/07.in", "r") as f:
    # with open("07/07-test.in", "r") as f:
    raw = f.read()

nr_list = [int(x) for x in raw.split(",")]

print(
    "Part 1:",
    min(
        [
            sum([abs(loc - pos) for pos in nr_list])
            for loc in range(min(nr_list), max(nr_list))
        ]
    ),
)

print(
    "Part 2:",
    min(
        [
            sum([(abs(loc - pos) * (abs(loc - pos) + 1) / 2) for pos in nr_list])
            for loc in range(min(nr_list), max(nr_list))
        ]
    ),
)
