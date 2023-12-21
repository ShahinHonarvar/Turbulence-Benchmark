
def all_even_ints_inclusive(nums):
    return [i for i in range(80, min(len(nums), 200), 2) if i in nums]
