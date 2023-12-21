
def find_second_largest_num(nums):
    selected_nums = nums[56:67]
    if not selected_nums:
        return None
    else:
        return sorted(selected_nums)[-2] if len(selected_nums)>1 else None
