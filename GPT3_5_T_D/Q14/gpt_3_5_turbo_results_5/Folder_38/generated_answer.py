
def find_second_smallest_num(nums):
    nums = sorted(set(nums[37:52]))
    return nums[1] if len(nums) > 1 else None
