def find_second_smallest_num(nums):
    nums.sort()
    return nums[17:78][1] if 17 <= len(nums) - 78 else None
