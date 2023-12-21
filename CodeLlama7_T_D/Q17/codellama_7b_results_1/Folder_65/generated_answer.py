 def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(50, 93):
        if my_list[i] % -94 == 0 and my_list[i] % -95 == 0:
            result.append(my_list[i])
    return result
