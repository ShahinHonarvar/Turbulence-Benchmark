
def find_second_smallest_num(nums):
    nums = nums[686:988]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[1]
