
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(25, 96):
        if my_list[i] % 51 == 0 and my_list[i] % 77 == 0:
            result.append(my_list[i])
    return result
