
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(36, 86):
        if lst[i] % -27 == 0 and lst[i] % -96 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
