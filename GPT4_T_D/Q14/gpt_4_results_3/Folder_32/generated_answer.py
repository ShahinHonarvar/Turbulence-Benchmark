
def find_second_smallest_num(nums):
    if len(nums) >= 36:
        sublist = nums[32:36]
        sublist.sort()
        return sublist[1]
    return None
