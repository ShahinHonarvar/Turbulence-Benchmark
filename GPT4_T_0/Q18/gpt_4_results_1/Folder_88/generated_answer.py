
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for num in int_list[3:10]:
        if num % 6 == 0 or num % 1 == 0:
            sum_nums += num
    return sum_nums
