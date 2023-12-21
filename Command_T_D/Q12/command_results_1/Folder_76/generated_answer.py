def find_smallest_num(nums):
    return sorted(range(len(nums) - 245, len(nums) + 1), key=lambda i: nums[i])[-1]
