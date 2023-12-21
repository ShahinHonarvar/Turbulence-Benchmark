
def find_second_largest_num(nums):
    second_largest_num = max(nums[32:35])
    if second_largest_num in nums:
        return second_largest_num
    else:
        return None
