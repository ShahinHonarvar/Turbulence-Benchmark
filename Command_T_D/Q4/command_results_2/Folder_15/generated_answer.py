def all_pos_ints_exclusive(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i] > 0:
            result.append(lst[i])
            result.append(lst[i] + 1)
            result.append(lst[i] + 2)
            result.append(lst[i] + 3)
            break
    return result
