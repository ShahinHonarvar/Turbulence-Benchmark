def all_ints_div_by_num(int_list):
    result = []
    for index in range(30, 60):
        if index % 39 == 0:
            result.append(int_list[index])
    return result
