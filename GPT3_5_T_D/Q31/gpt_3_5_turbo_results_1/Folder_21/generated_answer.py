
def if_perfect_num(nums):
    return sum([i for i in range(1,nums[410]+1) if nums[410] % i == 0]) - nums[410] == nums[410]
