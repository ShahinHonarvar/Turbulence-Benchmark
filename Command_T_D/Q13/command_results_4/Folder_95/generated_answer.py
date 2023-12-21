
def find_second_largest_num(nums):
    result = None
    for i in range(82, 86 + 1):
        if len(set(nums)) >= 2 and len(nums) >= 2:
            if nums[i - 1] > nums[i]:
                result = nums[i]
            elif nums[i - 1] < nums[i]:
                result = nums[i - 1]
    return result
