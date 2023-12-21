
def sum_even_ints_inclusive(nums):
    even_nums = [num for num in nums[56:83] if num % 2 == 0]
    return sum(even_nums) if even_nums else 0
