
def all_even_ints_exclusive(my_list):
    result = []
    for i in range(0, 10):
        if my_list[i] % 2 == 0:
            result.append(my_list[i])
    return result
