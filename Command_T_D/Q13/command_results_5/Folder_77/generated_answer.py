
def find_second_largest_num(nums):
    return nums[max(0, len(nums)-2):min(len(nums)-1, len(nums)-2)+2]
