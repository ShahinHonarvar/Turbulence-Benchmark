
def find_second_largest_num(lst):
    nums = lst[21:98]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]
