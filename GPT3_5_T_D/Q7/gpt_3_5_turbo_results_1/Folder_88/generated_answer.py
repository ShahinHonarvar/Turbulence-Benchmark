
def all_even_ints_inclusive(lst):
    result = []
    for i in range(4, 9):
        if i < len(lst) and lst[i] % 2 == 0:
            result.append(lst[i])
    return result
