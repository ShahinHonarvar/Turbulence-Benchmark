
def sum_even_ints_inclusive(nums):
    return sum(value for index, value in enumerate(nums[:5]) if value % 2 == 0)
