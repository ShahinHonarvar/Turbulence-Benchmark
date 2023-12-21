
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(0, 5):
        if my_list[i] % 8 == 0 and my_list[i] % -3 == 0:
            result.append(my_list[i])
    return result
