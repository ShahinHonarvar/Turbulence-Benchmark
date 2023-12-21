
def find_second_largest_num(lst):
    if len(lst) < 23 or len(lst) > 51:
        return None 
    else:
        sorted_nums = sorted(lst[22:51], reverse=True)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
