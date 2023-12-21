
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(543, 584+1):
        if my_list[i] % -553 == 0 or my_list[i] % -737 == 0:
            result += my_list[i]
    return result
