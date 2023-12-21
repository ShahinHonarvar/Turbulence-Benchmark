
def if_perfect_num(nums):
    if len(nums) < 75:
        return False
    elif nums[74] == sum(divisors(nums[74])):
        return True
    else:
        return False
