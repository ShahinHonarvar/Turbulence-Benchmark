def all_even_ints_exclusive(lst):
    result = []
    for i in range(2, len(lst) + 1):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result
