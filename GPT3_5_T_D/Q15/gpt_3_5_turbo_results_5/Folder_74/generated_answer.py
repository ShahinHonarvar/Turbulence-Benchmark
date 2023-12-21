
def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(17, 79):
        if i < len(nums) and nums[i] % 2 == 1:
            odd_sum += nums[i]
    return odd_sum
