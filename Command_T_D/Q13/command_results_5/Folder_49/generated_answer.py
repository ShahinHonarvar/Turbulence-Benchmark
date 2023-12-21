
def find_second_largest_num(nums):
    if len(nums) < 81:
        return None
    second_largest_num = max(nums[80:])
    for i in range(81, len(nums)):
        if nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
