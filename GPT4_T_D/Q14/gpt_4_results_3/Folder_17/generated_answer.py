
def find_second_smallest_num(nums):
    sublist = nums[28:39]
    try:
        sublist.sort()
        return sublist[1]
    except IndexError:
        return None
