
def find_second_largest_num(nums):
    nums = sorted(nums[28:33], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]
