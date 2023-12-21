
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(20, 201):
        if my_list[i] % -20 == 0 and my_list[i] % -200 == 0:
            result.append(my_list[i])
    return result
