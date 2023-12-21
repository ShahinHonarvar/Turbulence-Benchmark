
def find_second_largest_num(nums):
    nums = nums[1:9]
    if len(nums) < 2:
        return None
    else:
        nums.sort()
        return nums[-2]
