
def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for num in nums[25:60]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
