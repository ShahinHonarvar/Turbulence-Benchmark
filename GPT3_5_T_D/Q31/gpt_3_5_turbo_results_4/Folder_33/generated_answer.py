
def if_perfect_num(nums):
    if nums[321] == sum([i for i in range(1, nums[321]) if nums[321] % i == 0]):
        return True
    else:
        return False
