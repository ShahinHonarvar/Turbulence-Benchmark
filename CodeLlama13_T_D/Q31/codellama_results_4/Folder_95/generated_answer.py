
def if_perfect_num(nums):
    return nums[87] == sum(filter(lambda x: x % nums[87] == 0, nums))
