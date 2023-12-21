
def all_even_ints_inclusive(lst):
    result = []
    for i in range(len(lst) - 5):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    if lst[i] % 2 == 0:
        result.append(lst[i])
    if lst[i + 1] % 2 == 0:
        result.append(lst[i + 1])
    return result
