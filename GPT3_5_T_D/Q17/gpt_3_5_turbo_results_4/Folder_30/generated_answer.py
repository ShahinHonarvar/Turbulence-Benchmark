
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(11, 77):
        if lst[i] % -81 == 0 and lst[i] % -94 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
