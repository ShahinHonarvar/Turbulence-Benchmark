
def find_second_largest_num(nums):
    if len(nums) >= 83:
        selection = nums[56:83]
        selection.sort()
        if len(selection) > 1:
            return selection[-2]
    return None
