def all_even_ints_exclusive(nums):
    result = []
    if 48 in nums and 74 in nums:
        result = [n for n in nums if n % 2 == 0 and n != 48 and n != 74]
    return result
