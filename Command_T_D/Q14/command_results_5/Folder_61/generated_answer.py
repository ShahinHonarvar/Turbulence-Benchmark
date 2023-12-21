def find_second_smallest_num(nums):
    return nums[nums.index(sorted(set(nums))[1])-1] if len(nums) > 1 else None
