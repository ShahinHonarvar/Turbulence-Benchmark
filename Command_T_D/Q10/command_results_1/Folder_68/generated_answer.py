def all_odd_ints_exclusive(nums):
    return [i for i in range(len(nums)) if i % 2 == 1 and i != 0 and i != 8]
