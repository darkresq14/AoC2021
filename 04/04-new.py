import numpy as np
from copy import deepcopy

with open("04/04.in", "r") as f:
    # with open("04/04-test.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n\n")]
nrs = [int(number) for number in nr_list.pop(0).split(",")]

nr_list = (b.split() for b in nr_list)

flat_list = [int(item) for sublist in nr_list for item in sublist]

matrix = np.array(flat_list)
matrix.shape = (-1, 5, 5)

matrix_checked = np.zeros(matrix.shape)


def game(numbers, matrix, p2=False):
    last_draw = 0
    last_bingo = 0
    last_matrix = 0

    for i in numbers:
        # print(f"{i} found on: {np.argwhere(boards == i)}")
        matrix_checked[matrix == i] = 1

        # Check Rows
        for index_line, line in enumerate(matrix_checked.sum(2)):
            for index_element, element in enumerate(line):
                last_bingo = [index_line, index_element, "row"]
                if last_bingo not in all_bingos:
                    all_bingos.append(last_bingo)
                if element == 5:
                    if p2 == False:
                        last_draw = i
                        last_matrix = deepcopy(matrix_checked)
                        return (last_draw, last_bingo, last_matrix)
                    else:
                        if index_line not in boards_won:
                            boards_won.append(index_line)
                            last_draw = i
                            last_matrix = deepcopy(matrix_checked)

                            if len(boards_won) == len(matrix):
                                return (last_draw, last_bingo, last_matrix)

        # Check Columns
        for index_line, line in enumerate(matrix_checked.sum(1)):
            for index_element, element in enumerate(line):
                if element == 5:
                    last_bingo = [index_line, index_element, "col"]
                    if last_bingo not in all_bingos:
                        all_bingos.append(last_bingo)
                    if p2 == False:
                        last_draw = i
                        last_matrix = deepcopy(matrix_checked)
                        return (last_draw, last_bingo, last_matrix)
                    else:
                        if index_line not in boards_won:
                            boards_won.append(index_line)
                            last_draw = i
                            last_matrix = deepcopy(matrix_checked)

                            if len(boards_won) == len(matrix):
                                return (last_draw, last_bingo, last_matrix)

    return (last_draw, last_bingo, last_matrix)


def calculate_score(matrix, last_won_matrix, last_bingo, last_draw):
    matrix_sum = 0
    for index_row, row in enumerate(matrix[last_bingo[0]]):
        for index_col, value in enumerate(row):
            if int(last_won_matrix[last_bingo[0]][index_row][index_col]) != 1:
                matrix_sum += value

    return matrix_sum * last_draw


boards_won = []
all_bingos = []

last_draw, last_bingo, last_matrix = game(nrs, matrix)

print(f"Part 1: {calculate_score(matrix, last_matrix, last_bingo, last_draw)}")

last_draw, last_bingo, last_matrix = game(nrs, matrix, True)

print(f"Part 2: {calculate_score(matrix, last_matrix, last_bingo, last_draw)}")
