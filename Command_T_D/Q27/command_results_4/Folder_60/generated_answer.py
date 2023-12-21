
def insert_after_index(nums):
    return [x for x in nums] + [74] + [x for x in nums[21+1:]]
