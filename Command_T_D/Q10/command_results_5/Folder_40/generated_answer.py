def all_odd_ints_exclusive(nums):
    result = [n for n in nums if n % 2]
    if len(result) == 0:
        result = []
    return result
