
def sum_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[6:7] if num % 2 != 0]
    return sum(odd_nums) if odd_nums else 0
