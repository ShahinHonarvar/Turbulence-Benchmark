
def sum_odd_ints_inclusive(nums):
    if len(nums) < 7:
        return 0
    odd_sum = 0
    for i in range(5,8):
        if nums[i] % 2 == 1:
            odd_sum += nums[i]
    return odd_sum
