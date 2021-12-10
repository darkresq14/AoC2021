import numpy as np
from copy import deepcopy

with open("05/05.in", "r") as f:
    # with open("05/05-test.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n")]

flat_list = [
    int(value)
    for value in " ".join(nr_list).replace(" -> ", " ").replace(",", " ").split()
]


def part1(numeros):
    i = 0
    while i < len(numeros):
        x1 = numeros[i]
        y1 = numeros[i + 1]
        x2 = numeros[i + 2]
        y2 = numeros[i + 3]
        i += 4

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                matrix1[y, x1] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                matrix1[y1, x] += 1


def part2(numeros):
    i = 0
    while i < len(numeros):
        x1 = numeros[i]
        y1 = numeros[i + 1]
        x2 = numeros[i + 2]
        y2 = numeros[i + 3]
        i += 4

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                matrix2[y, x1] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                matrix2[y1, x] += 1
        if abs(x1 - x2) == abs(y1 - y2):
            condition = True
            while condition:
                if x1 > x2 and y1 > y2:
                    matrix2[y1, x1] += 1
                    x1 -= 1
                    y1 -= 1
                elif x1 > x2 and y1 < y2:
                    matrix2[y1, x1] += 1
                    x1 -= 1
                    y1 += 1
                elif x1 < x2 and y1 > y2:
                    matrix2[y1, x1] += 1
                    x1 += 1
                    y1 -= 1
                elif x1 < x2 and y1 < y2:
                    matrix2[y1, x1] += 1
                    x1 += 1
                    y1 += 1
                if x1 == x2 or y1 == y2:
                    matrix2[y1, x1] += 1
                    condition = False


def calc_part1(local_matrix):
    return (local_matrix > 1).sum()


matrix1 = np.zeros((np.max(flat_list) + 1, np.max(flat_list) + 1))

part1(flat_list)

print(f"Part 1: {calc_part1(matrix1)}")

matrix2 = np.zeros((np.max(flat_list) + 1, np.max(flat_list) + 1))

part2(flat_list)

print(f"Part 2: {calc_part1(matrix2)}")
