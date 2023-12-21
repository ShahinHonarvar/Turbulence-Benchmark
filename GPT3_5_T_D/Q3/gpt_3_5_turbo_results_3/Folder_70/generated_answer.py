
def all_pos_ints_inclusive(lst):
    result = []
    for i in range(28, 33):
        if i < len(lst) and lst[i] > 0:
            result.append(lst[i])
    return result
