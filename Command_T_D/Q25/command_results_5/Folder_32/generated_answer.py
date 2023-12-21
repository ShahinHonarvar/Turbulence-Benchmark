
def insert_at_index(nums):
    return [i for i in nums[:76]] + [10.01] + [i for i in nums[76+1:]]
