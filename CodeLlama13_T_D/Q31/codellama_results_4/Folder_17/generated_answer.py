
def if_perfect_num(nums):
    return nums[632] == sum(filter(lambda x: x % nums[632] == 0, range(1, nums[632])))
