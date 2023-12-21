
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for num in int_list[25:71]:
        if num % 74 == 0 or num % 15 == 0:
            sum_nums += num
    return sum_nums
