
def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) < 7:
        return None
    else:
        return nums[6]
