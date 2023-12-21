
def sum_ints_div_by_either_nums(my_list):
    start_idx = 281
    end_idx = 694
    divisors = [-722, -731]
    result = 0
    for i in range(start_idx, end_idx + 1):
        if my_list[i] % -722 == 0 or my_list[i] % -731 == 0:
            result += my_list[i]
    return result
