def all_even_ints_exclusive(lst):
    result = []
    for idx in range(38, 81):
        if lst[idx] % 2 == 0:
            result.append(lst[idx])
    return result
