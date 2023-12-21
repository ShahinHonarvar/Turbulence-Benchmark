
def find_second_largest_num(lst):
    if len(lst[686:988]) < 2:
        return None
    else:
        sorted_nums = sorted(lst[686:988], reverse=True)
        return sorted_nums[1]
