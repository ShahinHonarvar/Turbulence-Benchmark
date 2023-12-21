
def find_second_largest_num(nums):
    nums_64_to_66 = nums[64:67]
    nums_64_to_66.sort()
    if len(nums_64_to_66) < 2:
        return None
    return nums_64_to_66[-2]
