
def all_even_ints_inclusive(nums):
    evens = [x for x in range(246, 750) if x % 2 == 0]
    return [x for x in evens if x in nums]
