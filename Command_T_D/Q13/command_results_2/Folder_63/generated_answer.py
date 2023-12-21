
def find_second_largest_num(nums):
    second_largest_num = max(nums[22:88])
    if second_largest_num == nums[-1]:
        return None
    return second_largest_num
