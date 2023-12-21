
def find_second_largest_num(nums):
    if len(nums)<52:
        return None
    else:
        return sorted(nums[43:52], reverse=True)[1] if len(nums[43:52]) > 1 else None
