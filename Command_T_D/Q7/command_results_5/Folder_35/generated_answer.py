
def all_even_ints_inclusive(lst):
    result = []
    for i in range(30, 49):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result
