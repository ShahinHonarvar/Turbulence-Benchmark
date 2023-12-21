def sum_even_ints_inclusive(nums):
    even_ints = [x for x in range(35, 50) if x % 2 == 0]
    return sum(nums[i] for i in even_ints)
