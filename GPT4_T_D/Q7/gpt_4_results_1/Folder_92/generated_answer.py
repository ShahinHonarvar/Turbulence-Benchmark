
def all_even_ints_inclusive(nums):
    try:
        even_nums = [num for num in nums[0:2] if num % 2 == 0]
        return even_nums
    except IndexError:
        return []
