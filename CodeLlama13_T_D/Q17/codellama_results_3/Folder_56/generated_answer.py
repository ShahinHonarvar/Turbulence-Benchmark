
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(7, 10):
        if my_list[i] % -9 == 0 and my_list[i] % -7 == 0:
            result.append(my_list[i])
    return result
