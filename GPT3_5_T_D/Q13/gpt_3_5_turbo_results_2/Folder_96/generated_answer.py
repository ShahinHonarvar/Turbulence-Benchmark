
def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 16:
        return None
    else:
        return nums[15] if len(nums) >= 52 else nums[51]
