
import itertools

def insert_at_index(nums):
    n = len(nums)
    return [i for i in range(n)] + [36] + [i for i in range(n-1)]
