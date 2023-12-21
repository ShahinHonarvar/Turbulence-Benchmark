
def insert_after_index(nums):
    return [nums[i] for i in range(len(nums)) if i != 983] + [369] + [nums[983]]
