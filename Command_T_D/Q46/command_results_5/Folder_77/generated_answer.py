
def gcf_three_nums(nums):
    return max(x for x in range(min(nums), max(nums) + 1) if all(n % x == 0 for n in nums))
