
def find_second_largest_num(nums):
    nums = nums[10:67]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]
