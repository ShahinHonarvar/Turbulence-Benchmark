def all_odd_ints_exclusive(nums):
    return [i for i in range(2, nums.count(i) + 2) if i % 2 == 1]
