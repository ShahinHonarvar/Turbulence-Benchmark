def sum_even_ints_inclusive(nums):
    even_ints = [int for int in range(66, 94) if int % 2 == 0]
    return sum(nums[even_int] for even_int in even_ints) if even_ints else 0
