
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 3:
        return None
    else:
        return nums[2]
