
def find_second_smallest_num(nums):
    nums = nums[28:41]
    if len(nums) < 2:
        return None
    else:
        nums.sort()
        return nums[1]
