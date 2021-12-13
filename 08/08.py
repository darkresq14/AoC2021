from itertools import permutations

with open("08/08.in", "r") as f:
    # with open("08/08-test.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n")]

dict_ssd_len = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

# Part 1
outputs = [a.split(" | ")[1] for a in nr_list]
len_dict = {}
for v in " ".join(outputs).split():
    len_dict[len(v)] = 1 if len_dict.get(len(v)) is None else len_dict.get(len(v)) + 1

print(
    f"Part 1: {sum([len_dict[dict_ssd_len[1]], len_dict[dict_ssd_len[4]], len_dict[dict_ssd_len[7]], len_dict[dict_ssd_len[8]]])}"
)

# Part 2
dict_ssd = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

# Copied over from https://dev.to/qviper/advent-of-code-2021-python-solution-day-8-76p + https://github.com/MasterMedo/aoc/blob/master/2021/day/8.py
# Did not quite understand how it works exactly

part2 = 0
for row in nr_list:
    signals, output = row.split("|")
    signals = [s.strip() for s in signals.strip().split(" ")]
    output = [s.strip() for s in output.strip().split(" ")]

    for permutation in permutations("abcdefg"):
        to = str.maketrans("abcdefg", "".join(permutation))
        a_ = ["".join(sorted(code.translate(to))) for code in signals]
        b_ = ["".join(sorted(code.translate(to))) for code in output]
        if all(code in dict_ssd for code in a_):
            part2 += int("".join(str(dict_ssd[code]) for code in b_))
            break

print(f"Part 2: {part2}")