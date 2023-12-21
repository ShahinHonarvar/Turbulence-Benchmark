
def find_second_largest_num(nums):
    if len(nums[59:98]) == 0:
        return None
    else:
        nums_sorted = sorted(nums[59:98], reverse=True)
        return nums_sorted[1] if len(nums_sorted) > 1 else None
