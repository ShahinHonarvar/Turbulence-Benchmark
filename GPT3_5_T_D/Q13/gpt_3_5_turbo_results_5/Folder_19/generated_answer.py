
def find_second_largest_num(nums):
    nums = nums[3:6]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]
