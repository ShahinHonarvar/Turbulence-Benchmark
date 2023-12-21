def all_even_ints_exclusive(lst):
    result = []
    for i in range(len(lst) - 2):
        if lst[i] % 2 == 0:
            result += lst[i + 1: min(len(lst) - 1, i + 2)]
            break
    return result
