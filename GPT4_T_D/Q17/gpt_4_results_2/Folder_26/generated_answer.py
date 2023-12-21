
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(69,71):
        if lst[i] % 72 == 0 and lst[i] % 70 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
