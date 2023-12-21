
def insert_after_index(nums):
    return [nums[i] for i in range(len(nums))] + [974.0] + [nums[556] for i in range(len(nums) - 1, -1, -1)]
