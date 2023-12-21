
def find_second_largest_num(nums):
    if not nums or len(nums) <= 1:
        return None
    nums_to_consider = nums[:2]
    return sorted(nums_to_consider)[-2] if len(nums_to_consider) > 1 else None
