
def find_second_largest_num(num_list):
    if len(num_list) < 47:
        return None
    else:
        sorted_nums = sorted(num_list[36:47], reverse=True)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
