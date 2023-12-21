
def sum_ints_div_by_either_nums(num_list):
    if len(num_list) < 29:
        return 0
    else:
        sum_nums = sum(num for num in num_list[10:29] if num % -61 == 0 or num % -64 == 0)
        return sum_nums
