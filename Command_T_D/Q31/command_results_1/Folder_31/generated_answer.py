import re
def if_perfect_num(nums):
    # If there are less than 66 elements, return False
    if len(nums) < 66:
        return False
    # If the list is longer than 66 elements, check if the 66th element is a perfect number
    return nums[65] == int(re.sub(r'([0-9]+)0', r'\1', str(nums[65])))
