
def find_second_largest_num(lst):
    nums = lst[32:36]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[-2]
