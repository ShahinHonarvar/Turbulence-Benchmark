
def all_even_ints_inclusive(lst):
    result = []
    for i in range(52, 71):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result
