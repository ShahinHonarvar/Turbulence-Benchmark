
def find_second_largest_num(nums):
    nums = nums[639:976]
    if len(nums) > 1:
        nums.sort()
        return nums[-2]
    else:
        return None
