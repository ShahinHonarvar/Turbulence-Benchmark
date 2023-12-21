
def find_second_largest_num(nums):
    if len(nums) < 21:
        return None
    else:
        nums = nums[20:31]
        if len(nums) < 2:
            return None
        else:
            nums.sort()
            return nums[-2]
