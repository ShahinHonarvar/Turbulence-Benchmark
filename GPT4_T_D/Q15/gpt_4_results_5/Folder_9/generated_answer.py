
def sum_odd_ints_inclusive(nums):
    summ = 0
    for i in range(70, min(201, len(nums))):
        if nums[i] % 2 != 0:
            summ += nums[i]
    return summ
