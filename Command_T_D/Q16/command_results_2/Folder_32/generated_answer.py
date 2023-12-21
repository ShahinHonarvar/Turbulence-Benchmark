def sum_even_ints_inclusive(nums):
    even_ints = [x for x in range(21, 97) if x % 2 == 0]
    return sum(nums[even_int] for even_int in even_ints)
