
def insert_after_index(nums):
    return nums[:2] + [8] + nums[2:-2] + [8] + nums[-2:]
