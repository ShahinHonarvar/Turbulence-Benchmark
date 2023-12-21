def all_odd_ints_inclusive(nums):
    odd = [n for n in nums if n % 2 == 1]
    return odd[max(0, len(odd) - 310):min(len(odd) - 1, len(odd) - 370)]
