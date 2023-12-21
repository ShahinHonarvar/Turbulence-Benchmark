
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(46, 92):
        if my_list[i] % 67 == 0 and my_list[i] % 15 == 0:
            result.append(my_list[i])
    return result
