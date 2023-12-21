
def all_even_ints_inclusive(int_list):
    result = []
    for i in range(29, 51):
        if i % 2 == 0:
            result.append(int_list[i])
    return result
