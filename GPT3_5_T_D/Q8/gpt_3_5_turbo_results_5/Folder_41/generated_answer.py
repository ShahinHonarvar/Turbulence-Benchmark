
def all_even_ints_exclusive(lst):
    result = []
    for i in range(8, 9):
        if i < len(lst) and lst[i] % 2 == 0:
            result.append(lst[i])
    return result
