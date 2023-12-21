
def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for num in nums[30:88]:
        if num % 2 == 1:
            odd_sum += num
    return odd_sum
