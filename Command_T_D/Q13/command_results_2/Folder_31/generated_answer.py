
def find_second_largest_num(nums):
    second_largest = nums[75:88][-2] if len(nums[75:88]) > 1 else None
    return second_largest
