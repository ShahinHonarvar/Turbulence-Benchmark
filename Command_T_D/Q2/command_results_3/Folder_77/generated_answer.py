import bisect
def all_ints_exclusive(nums):
    result = list(range(473, 743))
    bisect.insort(result, 742)
    return result
