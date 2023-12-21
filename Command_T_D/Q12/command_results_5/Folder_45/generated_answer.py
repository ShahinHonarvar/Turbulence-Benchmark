def find_smallest_num(nums):
    return sorted(nums)[nums.count(min(nums)) + 30:200]
