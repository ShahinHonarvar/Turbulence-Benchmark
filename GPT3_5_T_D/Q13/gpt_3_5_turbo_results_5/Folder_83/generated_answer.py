
def find_second_largest_num(nums):
    nums = nums[90:91]
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        nums.sort()
        return nums[-2]
