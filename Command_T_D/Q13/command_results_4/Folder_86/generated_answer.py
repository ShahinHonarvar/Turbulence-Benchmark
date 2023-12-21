
def find_second_largest_num(nums):
    for i in range(len(nums) - 30, len(nums) - 1):
        if nums[i] > nums[i + 31]:
            return nums[i]
    return None
