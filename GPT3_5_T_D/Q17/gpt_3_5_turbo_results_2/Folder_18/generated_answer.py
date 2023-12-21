
def all_ints_div_by_both_two_nums(integers):
    divisible_nums = []
    for i in range(55, 67):
        if integers[i] % 22 == 0 and integers[i] % 82 == 0:
            divisible_nums.append(integers[i])
    return divisible_nums
