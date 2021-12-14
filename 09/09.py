import numpy as np

with open("09/09.in", "r") as f:
    # with open("09/09-test.in", "r") as f:
    raw = f.read()

nr_list = [x for x in raw.split("\n")]

# print(nr_list)

row_length = len(nr_list[0])
df = np.array([int(x) for sublist in nr_list for x in sublist])
df = df.reshape(-1, row_length)

# print(df)


def Part1(p1_df):
    risk_sum = 0
    for i in range(len(p1_df)):
        for j in range(len(p1_df[i])):
            if i == 0:
                if j == 0:
                    if p1_df[i][j] < p1_df[i + 1][j] and p1_df[i][j] < p1_df[i][j + 1]:
                        risk_sum += p1_df[i][j] + 1
                elif j == len(p1_df[i]) - 1:
                    if p1_df[i][j] < p1_df[i + 1][j] and p1_df[i][j] < p1_df[i][j - 1]:
                        risk_sum += p1_df[i][j] + 1
                elif (
                    p1_df[i][j] < p1_df[i + 1][j]
                    and p1_df[i][j] < p1_df[i][j - 1]
                    and p1_df[i][j] < p1_df[i][j + 1]
                ):
                    risk_sum += p1_df[i][j] + 1
            elif i == len(p1_df) - 1:
                if j == 0:
                    if p1_df[i][j] < p1_df[i - 1][j] and p1_df[i][j] < p1_df[i][j + 1]:
                        risk_sum += p1_df[i][j] + 1
                elif j == len(p1_df[i]) - 1:
                    if p1_df[i][j] < p1_df[i - 1][j] and p1_df[i][j] < p1_df[i][j - 1]:
                        risk_sum += p1_df[i][j] + 1
                elif (
                    p1_df[i][j] < p1_df[i - 1][j]
                    and p1_df[i][j] < p1_df[i][j - 1]
                    and p1_df[i][j] < p1_df[i][j + 1]
                ):
                    risk_sum += p1_df[i][j] + 1
            elif j == 0:
                if (
                    p1_df[i][j] < p1_df[i - 1][j]
                    and p1_df[i][j] < p1_df[i + 1][j]
                    and p1_df[i][j] < p1_df[i][j + 1]
                ):
                    risk_sum += p1_df[i][j] + 1
            elif j == len(p1_df[i]) - 1:
                if (
                    p1_df[i][j] < p1_df[i - 1][j]
                    and p1_df[i][j] < p1_df[i + 1][j]
                    and p1_df[i][j] < p1_df[i][j - 1]
                ):
                    risk_sum += p1_df[i][j] + 1
            elif (
                p1_df[i][j] < p1_df[i - 1][j]
                and p1_df[i][j] < p1_df[i + 1][j]
                and p1_df[i][j] < p1_df[i][j - 1]
                and p1_df[i][j] < p1_df[i][j + 1]
            ):
                risk_sum += p1_df[i][j] + 1
    return risk_sum


print(f"Part 1: {Part1(df)}")

# Shameless copy from https://dev.to/qviper/advent-of-code-2021-python-solution-day-9-4amm

from scipy import ndimage

label, num_label = ndimage.label(df < 9)
size = np.bincount(label.ravel())

top3 = sorted(size[1:], reverse=True)[:3]
print(f"Part 2: {np.prod(top3)}")
