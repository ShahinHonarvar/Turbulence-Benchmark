
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(138, 425):
        if my_list[i] % -863 == 0 and my_list[i] % -329 == 0:
            result.append(my_list[i])
    return result
