
def find_second_smallest_num(num_list):
    if len(num_list[55:99]) > 1:
        sorted_nums = sorted(num_list[55:99])
        return sorted_nums[1]
    else:
        return None
