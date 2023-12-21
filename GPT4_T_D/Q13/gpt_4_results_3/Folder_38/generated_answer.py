
def find_second_largest_num(lst):
    nums = lst[22:64]
    if len(nums)<2:
        return None
    else:
        nums.sort()
        return nums[-2]
