
def find_second_smallest_num(nums):
    if len(nums) < 49:
        return None
    sublist = nums[30:49]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]
