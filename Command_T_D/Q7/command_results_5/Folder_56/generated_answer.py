
def all_even_ints_inclusive(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result
