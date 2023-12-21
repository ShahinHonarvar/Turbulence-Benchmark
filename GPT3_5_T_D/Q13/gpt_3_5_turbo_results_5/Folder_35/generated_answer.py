
def find_second_largest_num(nums):
    nums = nums[30:49]
    if len(nums) < 2:
        return None
    max_num = max(nums)
    nums.remove(max_num)
    return max(nums)
