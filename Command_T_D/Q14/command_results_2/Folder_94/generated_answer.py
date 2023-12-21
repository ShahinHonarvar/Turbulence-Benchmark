def find_second_smallest_num(nums):
    return nums[nums.index(sorted(set(nums)[52:72])[1]) - 1] if nums.index(sorted(set(nums)[52:72])[1]) - 1 != -1 else None
