
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(90, 98):
        if my_list[i] % 13 == 0 and my_list[i] % 35 == 0:
            result.append(my_list[i])
    return result
