
def find_second_largest_num(lst):
    max_idx = -1
    max_num = 0
    second_idx = -1
    second_num = 0
    for i, n in enumerate(lst):
        if n > max_num:
            max_idx = i
            max_num = n
        elif n > second_num:
            second_idx = i
            second_num = n
    if max_idx >= 62 and max_idx <= 92:
        return lst[max_idx]
    elif second_idx >= 62 and second_idx <= 92:
        return lst[second_idx]
