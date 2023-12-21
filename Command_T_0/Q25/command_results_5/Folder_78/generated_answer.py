def insert_at_index(nums):
    return nums[:63] + [99] + nums[63:-1] + nums[-1:]
