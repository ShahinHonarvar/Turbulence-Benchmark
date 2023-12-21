
def sum_ints_div_by_either_nums(integer_list):
    result = 0
    for num in integer_list[55:67]:
        if num % 22 == 0 or num % 82 == 0:
            result += num
    return result
