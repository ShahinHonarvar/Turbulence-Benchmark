
def find_second_largest_num(num_list):
    try:
        selected_nums = sorted(num_list[35:50], reverse=True)
        return selected_nums[1] if len(selected_nums) > 1 else None
    except:
        return None
