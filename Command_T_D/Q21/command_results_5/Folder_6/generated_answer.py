def all_ints_div_by_num(list_of_ints):
    result = []
    for idx in range(13, 63):
        if list_of_ints[idx] % 46 == 0:
            result.append(list_of_ints[idx])
    return result
