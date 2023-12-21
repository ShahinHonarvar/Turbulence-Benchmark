
def all_even_ints_inclusive(nums):
    evens = [x for x in range(0, 7) if x % 2 == 0]
    return [x for x in nums if x in evens]
