
def all_even_ints_inclusive(my_list):
    result = []
    for i in range(50, 55):
        if my_list[i] % 2 == 0:
            result.append(my_list[i])
    return result
