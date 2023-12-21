
def if_perfect_num(nums):
    return nums[985] == sum(filter(lambda x: x <= nums[985], range(1, int(nums[985])**0.5 + 1)))
