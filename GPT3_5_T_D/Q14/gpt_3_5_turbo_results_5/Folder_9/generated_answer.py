
def find_second_smallest_num(nums):
    sublist = sorted(nums[70:201])
    if len(sublist) < 2:
        return None
    return sublist[1]
