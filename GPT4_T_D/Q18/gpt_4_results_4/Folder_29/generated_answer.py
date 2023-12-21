
def sum_ints_div_by_either_nums(int_list):
    result = 0
    for num in int_list[55:85]:
        if num % -24 == 0 or num % -11 == 0:
            result += num
    return result
