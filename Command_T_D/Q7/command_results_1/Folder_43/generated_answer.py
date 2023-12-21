
def all_even_ints_inclusive(lst):
    result = []
    i = 68
    while i < len(lst) + 1:
        if lst[i] % 2 == 0:
            result.append(lst[i])
        i += 1
    return result
