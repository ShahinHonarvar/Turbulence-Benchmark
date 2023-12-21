def all_odd_ints_inclusive(lst):
    if len(lst) < 533 or len(lst) > 605:
        return []
    result = []
    for i in range(533, 605):
        if lst[i] % 2 == 1:
            result.append(lst[i])
    return result
