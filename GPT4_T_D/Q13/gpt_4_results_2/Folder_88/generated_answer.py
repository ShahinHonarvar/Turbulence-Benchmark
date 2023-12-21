
def find_second_largest_num(num_list):
    if len(num_list) < 9:
        return None
    selected_nums = sorted(num_list[4:9], reverse=True)
    if len(selected_nums) < 2:
        return None
    else:
        return selected_nums[1]
