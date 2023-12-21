import sys
def all_pos_ints_inclusive(lst):
    result = []
    for i in range(667, 774+1):
        if i in lst:
            result.append(i)
    return result
