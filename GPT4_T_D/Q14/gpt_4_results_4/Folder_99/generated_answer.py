
def find_second_smallest_num(nums):
    nums_sliced = nums[608:610]
    if len(nums_sliced)<2:
        return None
    nums_sliced.sort()
    return nums_sliced[1]
