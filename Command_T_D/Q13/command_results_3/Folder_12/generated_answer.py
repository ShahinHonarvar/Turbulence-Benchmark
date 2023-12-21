
def find_second_largest_num(nums):
    second_largest = nums[14:65][-2] if len(nums[14:65]) > 1 else None
    return second_largest
