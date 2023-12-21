def all_ints_not_div_by_num(list_of_ints):
    result = []
    for index in range(24, 45):
        if index % -72 != 0:
            result.append(list_of_ints[index])
    return result
