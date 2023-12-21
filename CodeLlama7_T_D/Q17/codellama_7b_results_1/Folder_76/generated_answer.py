
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(250, 630):
        if my_list[i] % 850 == 0 and my_list[i] % 587 == 0:
            result.append(my_list[i])
    return result
