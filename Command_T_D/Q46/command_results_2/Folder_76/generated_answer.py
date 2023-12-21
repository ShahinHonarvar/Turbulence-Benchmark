
def gcf_three_nums(nums):
    return max(x for x in range(min(nums), max(nums) + 1) if all(num % x == 0 for num in nums))
