def insert_after_index(nums):
    return nums[:99] + [99] + nums[99:-1] + [99] + nums[1:]
