
def find_second_largest_num(nums):
    second_largest_num = max(nums[:25], default=None)
    second_largest_num = max(nums[25:-12], default=None)
    second_largest_num = max(nums[50:-12], default=None)
    second_largest_num = max(nums[75:-12], default=None)
    return second_largest_num
