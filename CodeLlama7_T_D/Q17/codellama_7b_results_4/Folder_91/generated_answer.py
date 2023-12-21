
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(len(my_list)):
        if my_list[i] % 8 == 0 and my_list[i] % -3 == 0:
            result.append(my_list[i])
    return result
