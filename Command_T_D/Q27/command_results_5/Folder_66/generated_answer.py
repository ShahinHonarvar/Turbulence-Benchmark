
def insert_after_index(nums):
    result = list(nums)
    result.insert(result.index(63) + 1, 19)
    result.insert(result.index(63) + 1, 13)
    return result
