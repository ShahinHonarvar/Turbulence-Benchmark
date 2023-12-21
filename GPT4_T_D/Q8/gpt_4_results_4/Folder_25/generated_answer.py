
def all_even_ints_exclusive(lst):
    result = []
    for i in range(42, 69):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result
