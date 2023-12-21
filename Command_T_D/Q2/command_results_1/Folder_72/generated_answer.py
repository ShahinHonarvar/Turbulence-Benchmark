def all_ints_exclusive(nums):
    return list(range(25, nums.count(25)+1, 25)) + list(range(75, nums.count(75)+1, 25))
