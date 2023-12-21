
def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(22, 51):
        if i < len(nums) and nums[i] % 2 == 0:
            even_sum += nums[i]
    return even_sum
