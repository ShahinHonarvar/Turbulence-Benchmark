
def find_second_smallest_num(nums):
    if len(nums[28:41])<2:
        return None
    else:
        return sorted(nums[28:41])[1]
