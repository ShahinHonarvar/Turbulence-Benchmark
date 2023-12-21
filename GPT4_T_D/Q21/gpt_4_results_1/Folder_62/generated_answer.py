
def all_ints_div_by_num(num_list):
    result = []
    for i in range(87, 90):
        if num_list[i] % 55 == 0:
            result.append(num_list[i])
    return result
