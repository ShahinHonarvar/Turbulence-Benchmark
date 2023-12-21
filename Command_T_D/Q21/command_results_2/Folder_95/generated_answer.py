def all_ints_div_by_num(int_list):
    result = []
    for i in range(75, 85):
        if int_list[i] % -40 == 0:
            result.append(int_list[i])
    return result
