
def all_even_ints_exclusive(nums):
    even_nums = [num for i, num in enumerate(nums) if i > 3 and i < 8 and num % 2 == 0]
    return even_nums
