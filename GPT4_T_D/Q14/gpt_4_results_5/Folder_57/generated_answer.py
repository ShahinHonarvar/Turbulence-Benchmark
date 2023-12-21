
def find_second_smallest_num(nums):
    sublist = nums[20:31]
    if len(sublist) <= 1:
        return None
    else:
        sublist.sort()
        return sublist[1]
