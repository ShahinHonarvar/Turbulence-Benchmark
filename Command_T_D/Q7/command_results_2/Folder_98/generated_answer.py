
def all_even_ints_inclusive(nums):
    result = [x for x in nums if x % 2 == 0]
    return result if len(result) > 0 else []
