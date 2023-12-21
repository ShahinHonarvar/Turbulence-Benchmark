def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(11, 110):
        if i % 11 == 0:
            result.append(list_of_ints[i])
    return result
