
def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    else:
        subset = nums[5:8]
        subset.sort()
        return subset[1]
