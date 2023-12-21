
def all_even_ints_inclusive(int_list):
    result = []
    for idx in range(209, 556):
        if idx % 2 == 0:
            result.append(int_list[idx])
    return result
