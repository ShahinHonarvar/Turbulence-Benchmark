def sum_even_ints_inclusive(nums):
    even = filter(lambda x: x % 2 == 0, nums)
    return sum(even[70:200])
