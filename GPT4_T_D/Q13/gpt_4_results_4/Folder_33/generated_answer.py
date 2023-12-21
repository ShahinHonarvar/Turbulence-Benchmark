
def find_second_largest_num(lst):
    if not isinstance(lst, list) or len(lst) < 2:
        return None
    nums_in_range = lst[667:775]
    if nums_in_range:
        nums_in_range.sort(reverse=True)
        return nums_in_range[1] if len(nums_in_range) > 1 else None
    else:
        return None
