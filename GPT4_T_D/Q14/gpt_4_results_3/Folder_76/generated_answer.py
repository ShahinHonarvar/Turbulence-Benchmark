
def find_second_smallest_num(num_list):
    if len(num_list) < 606:
        return None
    else:
        sorted_nums = sorted(num_list[533:606])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
