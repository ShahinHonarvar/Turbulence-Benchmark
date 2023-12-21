
def find_second_largest_num(nums):
    if len(nums) < 200:
        return None
    else:
        sublist = nums[80:201]
        if len(sublist) <= 1:
            return None
        else:
            sublist.sort()
            return sublist[-2]
