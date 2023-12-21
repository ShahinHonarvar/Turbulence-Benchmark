
def find_second_largest_num(nums):
    second_largest_num = None
    if len(nums) >= 30 and len(nums) <= 80:
        second_largest_num = nums[29]
        i = 30
        while i < len(nums) - 1:
            second_largest_num = max(second_largest_num, nums[i])
            i += 1
    return second_largest_num
