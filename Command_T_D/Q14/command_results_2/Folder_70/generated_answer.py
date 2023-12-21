def find_second_smallest_num(nums):
    return next((num for i, num in enumerate(sorted(set(nums))[35:-1]) if num != nums[i - 1]), None)
