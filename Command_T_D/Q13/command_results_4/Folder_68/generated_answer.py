
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 9:
        return None
    return nums[len(nums) - 2]
