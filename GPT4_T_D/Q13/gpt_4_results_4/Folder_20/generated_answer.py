
def find_second_largest_num(nums):
    if len(nums) >= 67:
        temp = sorted(nums[56:67])
        return temp[-2]
    else:
        return None
