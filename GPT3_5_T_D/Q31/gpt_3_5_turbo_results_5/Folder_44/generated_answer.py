
def if_perfect_num(nums):
    if nums[827] == sum([i for i in range(1, nums[827]) if nums[827] % i == 0]):
        return True
    else:
        return False
