
def all_even_ints_inclusive(my_list):
    result = []
    for i in range(31, 35):
        if my_list[i] % 2 == 0:
            result.append(my_list[i])
    return result
