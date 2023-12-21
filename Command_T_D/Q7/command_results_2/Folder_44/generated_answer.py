
def all_even_ints_inclusive(lst):
    result = []
    for i in range(13, 69):
        if i % 2 == 0:
            result.append(lst[i])
    return result
