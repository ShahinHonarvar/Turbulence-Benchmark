
def find_second_largest_num(nums):
    nums = nums[0:10]
    nums = sorted(nums)
    if len(nums) < 2:
        return None
    else:
        return nums[-2]
