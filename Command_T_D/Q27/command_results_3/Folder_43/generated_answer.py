
def insert_after_index(nums):
    result = list(nums)
    result.insert(result.index(29) + 1, 28)
    result.insert(result.index(29) + 1, 53)
    return result
