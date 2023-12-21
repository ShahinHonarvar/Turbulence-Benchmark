
def sum_ints_div_by_either_nums(lst):
    valid_nums = [-90, -67]
    sum_nums = 0
    for i in range(69, 98):
        if lst[i] % valid_nums[0] == 0 or lst[i] % valid_nums[1] == 0:
            sum_nums += lst[i]
    return sum_nums
