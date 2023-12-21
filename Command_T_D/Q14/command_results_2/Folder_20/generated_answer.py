def find_second_smallest_num(nums):
    idx = 75
    while idx < len(nums) - 1:
        if idx < len(nums) - 2:
            if nums[idx] > nums[idx + 1]:
                return nums[idx + 1]
        else:
            return nums[idx]
