
def insert_after_index(nums):
    return [x for x in nums] + [15, 51] + [x for x in nums[76+1:]]
