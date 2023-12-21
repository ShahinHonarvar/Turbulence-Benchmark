import itertools
def composite_nums_between_indices(nums):
    return set(filter(is_composite, nums[75:94]))
def is_composite(num):
    # check for divisibility by prime numbers
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
