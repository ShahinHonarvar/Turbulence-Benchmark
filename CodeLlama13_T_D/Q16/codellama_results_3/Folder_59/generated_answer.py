
def sum_even_ints_inclusive(nums):
    return sum(i for i in nums[:10] if i % 2 == 0) or 0
