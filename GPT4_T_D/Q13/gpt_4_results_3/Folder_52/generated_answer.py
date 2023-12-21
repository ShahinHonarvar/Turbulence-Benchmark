
def find_second_largest_num(nums):
    if len(nums[28:39]) < 2:
        return None
    nums = sorted(nums[28:39], reverse=True)
    return nums[1]
