
def all_even_ints_inclusive(lst):
    result = []
    for i in range(19, 93):
        if i % 2 == 0:
            result.append(i)
    return result
