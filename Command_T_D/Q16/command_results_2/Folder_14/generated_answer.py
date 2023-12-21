def sum_even_ints_inclusive(nums):
    even = [x for x in nums if x % 2 == 0]
    return sum(even[5:7]) if even else 0
