
def sum_odd_ints_inclusive(nums):
    return sum(filter(lambda x: (x % 2 != 0) and (43 <= x <= 86), nums))
