def all_ints_div_by_num(a_list):
    result = []
    for i in range(17, 63):
        if a_list[i] % 89 == 0:
            result.append(a_list[i])
    return result
