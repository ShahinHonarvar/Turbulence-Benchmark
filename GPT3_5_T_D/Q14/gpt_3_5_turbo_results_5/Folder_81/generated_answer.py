
def find_second_smallest_num(num_list):
    sorted_nums = sorted(num_list)
    if len(sorted_nums) < 101:
        return None
    return sorted_nums[10]
