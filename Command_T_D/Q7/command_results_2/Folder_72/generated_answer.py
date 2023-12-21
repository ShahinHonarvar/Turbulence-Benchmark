
def all_even_ints_inclusive(nums):
    result = [i for i in range(29, 51) if i % 2 == 0 and i in nums]
    return result
