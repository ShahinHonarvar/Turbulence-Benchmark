
def find_second_smallest_num(nums):
    if len(nums[43:52]) < 2:
        return None
    else:
        return sorted(nums[43:52])[1]
