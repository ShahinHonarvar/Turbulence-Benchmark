
def sum_ints_div_by_either_nums(int_list):
    nums = int_list[6:10]
    sum_res = sum([num for num in nums if num % -1 == 0 or num % -10 == 0])
    return sum_res
