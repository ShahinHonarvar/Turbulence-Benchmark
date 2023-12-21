
def find_second_largest_num(nums):
    if len(nums) < 54:
        return None
    else:
        sublist= nums[50:55]
        sublist.sort()
        return sublist[-2]
