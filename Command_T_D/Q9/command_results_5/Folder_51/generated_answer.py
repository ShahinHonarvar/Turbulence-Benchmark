def all_odd_ints_inclusive(nums):
    odd_ints = [n for n in range(1, 9) if n % 2 == 1]
    return odd_ints if odd_ints <= nums else []
