
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(10, 80):
        if my_list[i] % -74 == 0 and my_list[i] % -58 == 0:
            result.append(my_list[i])
    return result
