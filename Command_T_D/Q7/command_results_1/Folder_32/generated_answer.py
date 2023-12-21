
def all_even_ints_inclusive(nums):
    return [i for i in range(min(nums), max(nums)+1) if i % 2 == 0]
