
def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    nums = sorted(lst[4:9], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]
