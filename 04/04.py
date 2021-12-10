# from collections import defaultdict
from copy import deepcopy

# with open("04/04.in", "r") as f:
with open("04/04-test.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n\n")]

numbers_outer = nr_list[0].split(",")
boards_outer = {}
boards_list = nr_list[1:]

for index, board_outer in enumerate(boards_list):
    board_row = [i.split() for i in board_outer.split("\n")]
    boards_outer[index] = board_row

# print(boards_outer)
# print(numbers_outer)


def game(numbers, boards, part2=False):
    matched = {b: {i: [] for i in range(5)} for b in boards.keys()}
    matched_columns = {b: {i: [] for i in range(5)} for b in boards.keys()}
    part2_counter = {b: [] for b in boards.keys()}
    last_match_state = {}

    for number in numbers:
        # print(number)
        for dict_key in boards.keys():
            board = boards.get(dict_key)
            for row_index, row_value in enumerate(board):
                # print(row_index, row_value)
                if number in row_value:
                    matched_dict = matched[dict_key]
                    matched_dict.get(row_index).append(row_value.index(number))
                    matched_columns[dict_key][row_value.index(number)].append(1)
                    if len(matched_dict.get(row_index)) == 5:
                        part2_counter[dict_key].append(1)
                        if part2 is False:
                            # print(
                            #     f"Winning row in board {dict_key} row {row_index}: {matched_dict.get(row_index)}"
                            # )
                            return (
                                number,
                                matched[dict_key],
                                boards.get(dict_key),
                                "row",
                                row_index,
                            )
                        else:
                            if len(part2_counter[dict_key]) <= 1:
                                last_number = number
                                last_match_state = deepcopy(matched[dict_key])
                                print(f"Part2 unique winning state on board {dict_key}")
                                last_board = boards.get(dict_key)
                            else:
                                pass
                    if len(matched_columns[dict_key][row_value.index(number)]) == 5:
                        part2_counter[dict_key].append(1)
                        if part2 is False:
                            # print(
                            #     f"Winning column in board {dict_key} column {row_value.index(number)}"
                            # )
                            return (
                                number,
                                matched[dict_key],
                                boards.get(dict_key),
                                "column",
                                row_value.index(number),
                            )
                        else:
                            if len(part2_counter[dict_key]) <= 1:
                                last_number = number
                                last_match_state = deepcopy(matched[dict_key])
                                print(f"Part2 unique winning state on board {dict_key}")
                                last_board = boards.get(dict_key)
                            else:
                                pass

    return last_number, last_match_state, last_board


def calculate_score(numbers, last_number, board):
    numbers_picked = []
    for x in numbers:
        if x == last_number:
            numbers_picked.append(x)
            break
        else:
            numbers_picked.append(x)
    result = 0
    for line in board:
        for nr in line:
            if nr not in numbers_picked:
                result += int(nr)

    return result * int(last_number)


number, matched, board, rowCol, row_index = game(numbers_outer, boards_outer)

print(f"Part 1: {calculate_score(numbers_outer, number, board)}")
