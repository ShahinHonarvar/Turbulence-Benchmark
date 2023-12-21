
def find_second_largest_num(num_list):
    if 26 < len(num_list) < 42:
        return None
    else:
        sorted_nums = sorted(num_list[42:69], reverse=True)
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
