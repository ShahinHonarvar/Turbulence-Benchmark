def all_even_ints_exclusive(int_list):
    result = []
    for i in range(7, 9):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result
