
def all_ints_inclusive(nums):
    result = list(range(min(nums), max(nums)+1))
    return result[12:92] + result[:12] + result[92:]
