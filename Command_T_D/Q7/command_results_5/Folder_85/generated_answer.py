
def all_even_ints_inclusive(lst):
    result = []
    if lst[6] % 2 == 0 and lst[7] % 2 == 0:
        result.append(lst[6])
        result.append(lst[7])
    return result
