
def all_ints_div_by_num(lst):
    divisible_nums = []
    for num in lst[75:89]:
        if num % -27 == 0:
            divisible_nums.append(num)
    return divisible_nums
