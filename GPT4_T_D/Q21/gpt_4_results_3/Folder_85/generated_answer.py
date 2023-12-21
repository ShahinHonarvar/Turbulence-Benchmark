
def all_ints_div_by_num(lst):
    divisible_nums = []
    for i in lst[6:9]:
        if i % -9 == 0:
            divisible_nums.append(i)
    return divisible_nums
