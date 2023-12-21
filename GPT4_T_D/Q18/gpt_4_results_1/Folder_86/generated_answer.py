
def sum_ints_div_by_either_nums(integer_list):
    sum_divisible = 0
    for i in range(54, min(80, len(integer_list))):
        if integer_list[i] % 54 == 0 or integer_list[i] % 28 == 0:
            sum_divisible += integer_list[i]
    return sum_divisible
