
def find_second_smallest_num(nums):
    if len(nums[43:87])<2:
        return None
    nums_sorted = sorted(nums[43:87])
    return nums_sorted[1] if nums_sorted else None
