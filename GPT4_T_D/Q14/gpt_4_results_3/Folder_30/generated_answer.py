
def find_second_smallest_num(num_list):
    if len(num_list) < 53:
        return None
    else:
        selected_nums = sorted(num_list[26:53])
        if len(selected_nums) < 2:
            return None
        else:
            return selected_nums[1]
