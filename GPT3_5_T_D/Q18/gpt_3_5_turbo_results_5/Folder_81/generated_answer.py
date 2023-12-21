
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[10:101] if x % 10 == 0 or x % 100 == 0)
