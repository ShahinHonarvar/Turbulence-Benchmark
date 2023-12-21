
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(38, 53):
        if lst[i] % -41 == 0 and lst[i] % -47 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
