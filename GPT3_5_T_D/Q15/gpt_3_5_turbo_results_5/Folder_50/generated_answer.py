
def sum_odd_ints_inclusive(nums):
    sum = 0
    for num in nums[70:85]:
        if num % 2 != 0:
            sum += num
    return sum
