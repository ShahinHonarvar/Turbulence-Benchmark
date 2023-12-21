
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    second_largest_num = max(nums[:-1])
    second_largest_index = nums.index(second_largest_num)
    return second_largest_num
