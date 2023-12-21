
def all_ints_div_by_num(num_list):
    result = []
    for i in range(42, 90):
        if num_list[i] % -59 == 0:
            result.append(num_list[i])
    return result
