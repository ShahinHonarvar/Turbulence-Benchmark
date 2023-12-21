
def find_second_largest_num(nums):
    nums = sorted(nums[64:67])
    if len(nums) >= 2:
        return nums[-2]
    else:
        return None
