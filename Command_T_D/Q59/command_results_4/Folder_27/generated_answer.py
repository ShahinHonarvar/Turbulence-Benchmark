import itertools
def all_left_truncatable_prime(nums):
    return sorted(list(filter(lambda x: all(y == '9' for y in str(x)), itertools.chain(map(str, nums)))), reverse=True)
