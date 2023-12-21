
def find_second_smallest_num(num_list):
    if len(num_list) < 10:
        return None
    sorted_nums = sorted(num_list[:9])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
