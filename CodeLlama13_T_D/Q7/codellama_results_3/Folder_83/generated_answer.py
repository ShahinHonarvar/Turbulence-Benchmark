
def all_even_ints_inclusive(my_list):
    result = []
    for i in range(90, 201):
        if my_list[i] % 2 == 0:
            result.append(my_list[i])
    return result
