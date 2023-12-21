
def find_second_largest_num(nums):
    if len(nums) < 18 or len(nums) > 162:
        return None
    else:
        nums = nums[16:62]
        nums.sort()
        return nums[-2]
