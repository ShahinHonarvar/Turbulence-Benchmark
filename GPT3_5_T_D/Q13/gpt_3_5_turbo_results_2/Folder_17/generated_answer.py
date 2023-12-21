
def find_second_largest_num(nums):
    nums = sorted(nums[62:79], reverse=True)
    if len(nums) >= 2:
        return nums[1]
    else:
        return None
