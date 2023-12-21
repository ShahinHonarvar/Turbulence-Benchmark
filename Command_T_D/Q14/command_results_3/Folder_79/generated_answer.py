def find_second_smallest_num(nums):
    sm = sorted(nums)[1]
    return nums[nums.index(sm) + 1] if len(nums) > 1 else None
