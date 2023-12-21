
def sum_even_ints_inclusive(nums):
    even_nums = [num for num in nums[246:751] if num % 2 == 0]
    return sum(even_nums)
