def all_even_ints_exclusive(nums):
    evens = [i for i in range(25, 80) if i % 2 == 0]
    return [x for x in nums[evens[0]:evens[-1]] if x % 2 == 0]
