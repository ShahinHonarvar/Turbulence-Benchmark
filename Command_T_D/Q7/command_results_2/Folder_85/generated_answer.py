
def all_even_ints_inclusive(nums):
    even_ints = [x for x in range(6, 8) if x % 2 == 0]
    return [x for x in nums if x in even_ints]
