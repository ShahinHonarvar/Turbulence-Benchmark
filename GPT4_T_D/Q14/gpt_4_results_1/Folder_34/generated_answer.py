
def find_second_smallest_num(nums):
    if 60 < len(nums) <= 200:
        nums = sorted(nums[60:201])
        return None if len(nums) < 2 else nums[1]
    else:
        return None
