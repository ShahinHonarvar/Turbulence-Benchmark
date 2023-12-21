import sys
def all_ints_div_by_num(ints):
    indices = []
    for i in range(70, 71 + 1):
        if ints[i] % 85 == 0:
            indices.append(i)
    return indices
