def sum_even_ints_inclusive(nums):
    even = [n for n in range(527, 538) if n % 2 == 0]
    return sum(nums[even[0] : even[1] + 1])
