
def sum_ints_div_by_either_nums(nums):
    return sum(nums[x:x + 10] for x in range(138, 425, 10) if (x % 10) % 2)
