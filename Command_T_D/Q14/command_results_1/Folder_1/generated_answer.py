def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[34]) - 1] if nums[nums.index(sorted(nums)[34]) - 1] in nums[34:55] else None
