
def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    if len(nums)>1:
        for num in nums[1:2]:
            if num%2 != 0:
                odd_sum += num
    return odd_sum
