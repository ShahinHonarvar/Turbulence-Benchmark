
def find_second_largest_num(nums):
    if len(nums) < 2 or not 4<=len(nums)<=5:
        return None
    nums = nums[4:5]
    nums.sort()
    return nums[-2] if len(nums) > 1 else None
