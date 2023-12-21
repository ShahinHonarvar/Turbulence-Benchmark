def all_pos_ints_exclusive(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] > 14 and lst[i] < 100:
            result.append(lst[i])
    return result
