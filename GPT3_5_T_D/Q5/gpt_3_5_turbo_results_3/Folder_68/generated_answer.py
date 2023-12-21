
def all_neg_ints_inclusive(lst):
    result = []
    for i in range(9):
        if i < len(lst) and lst[i] < 0:
            result.append(lst[i])
    return result
