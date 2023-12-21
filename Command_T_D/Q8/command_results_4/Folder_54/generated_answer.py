def all_even_ints_exclusive(nums):
    even_ints = [i for i in range(27, 35) if i % 2 == 0]
    return [nums[i] for i in even_ints] if even_ints else []
