
def insert_after_index(nums):
    return [i for i in nums[:4]] + [7] + [i for i in nums[4:-1]] + [nums[-1]]
