
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(31, 51):
        if lst[i] % 81 == 0 and lst[i] % 64 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
