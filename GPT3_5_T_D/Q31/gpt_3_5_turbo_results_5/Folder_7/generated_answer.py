
def if_perfect_num(nums):
    return nums[850] == sum([i for i in range(1, nums[850]) if nums[850] % i == 0])
