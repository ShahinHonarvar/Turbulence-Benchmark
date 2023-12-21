
def all_even_ints_inclusive(int_list):
    result = []
    for val in int_list[10:67]:
        if val % 2 == 0:
            result.append(val)
    return result
