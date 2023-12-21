
def find_second_largest_num(num_list):
    selected_nums = num_list[25:60]
    if len(selected_nums) < 2:
        return None
    else:
        selected_nums.sort(reverse = True)
        return selected_nums[1]
