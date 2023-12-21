
def insert_after_index(nums):
    return [num for num in nums[:55]] + [54] + [num for num in nums[56:-1]] + [55]
