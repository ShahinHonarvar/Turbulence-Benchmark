
def find_second_largest_num(nums):
    if len(nums) < 92:
        return None
    else:
        sublist = nums[91:100]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[-2]
