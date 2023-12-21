
def sum_even_ints_inclusive(nums):
    if len(nums) < 89:
        nums.extend([0]*(89 - len(nums)))
    range_nums = nums[22:89]
    even_nums = [num for num in range_nums if num % 2 == 0]
    return sum(even_nums) if even_nums else 0
