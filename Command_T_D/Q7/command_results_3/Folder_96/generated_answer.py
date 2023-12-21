
def all_even_ints_inclusive(nums):
    even_ints = [x for x in range(50, 200) if x % 2 == 0]
    return [x for x in even_ints if x in nums]
