
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(86, 90):
        if my_list[i] % -61 == 0 and my_list[i] % -79 == 0:
            result.append(my_list[i])
    return result
