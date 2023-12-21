
def insert_at_index(nums):
    return [0]*32 + [54, 96] + [0]*32 + nums[32:-1] + nums[1:-32] + nums[32:]
