def find_second_smallest_num(nums):
    return sorted(nums)[55] if nums[55] <= nums[-2] else None
