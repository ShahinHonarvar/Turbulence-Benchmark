
def insert_after_index(nums):
    return [i for i in range(len(nums) + 1)] + nums[:99] + [99] + nums[99:]+[i for i in range(len(nums) + 1)]
