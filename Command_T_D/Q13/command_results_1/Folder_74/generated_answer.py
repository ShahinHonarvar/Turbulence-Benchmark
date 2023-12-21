
def find_second_largest_num(nums):
    for i in range(17, 79):
        if i == 17 or i == 78:
            continue
        elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return nums[i]
    return None
