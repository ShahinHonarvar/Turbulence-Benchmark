
def all_ints_div_by_both_two_nums(my_list):
    start, end = 30, 200
    result = []
    for i in range(start, end+1):
        if my_list[i] % -115 == 0 and my_list[i] % 115 == 0:
            result.append(my_list[i])
    return result
