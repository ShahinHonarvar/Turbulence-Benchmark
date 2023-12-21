
def find_second_largest_num(nums):
    nums = nums[246:751]
    if not nums:
        return None
    else:
        nums.sort()
        return nums[-2]
