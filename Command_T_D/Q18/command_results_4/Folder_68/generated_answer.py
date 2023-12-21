
def sum_ints_div_by_either_nums(nums):
    return sum(nums[7:7+i] for i in range(0, len(nums)-6) if any(n % 5 == 0 or n % 7 == 0 for n in nums[7:7+i]))
