
def find_second_largest_num(nums):
    nums = nums[246:751]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[-2]
