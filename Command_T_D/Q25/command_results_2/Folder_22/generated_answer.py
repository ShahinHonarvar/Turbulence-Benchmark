
def insert_at_index(nums):
    return nums[:85] + [27] + nums[85:-1] + [27] + nums[86:]
