
def sum_even_ints_inclusive(nums):
    even_nums = [num for num in nums[:8] if num % 2 == 0]
    if even_nums:
        return sum(even_nums)
    else:
        return 0
