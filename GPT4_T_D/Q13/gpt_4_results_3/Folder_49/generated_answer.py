
def find_second_largest_num(num_list):
    selected_nums = num_list[80:201]
    if selected_nums:
        selected_nums.sort()
        return selected_nums[-2] if len(selected_nums) > 1 else None
    return None
