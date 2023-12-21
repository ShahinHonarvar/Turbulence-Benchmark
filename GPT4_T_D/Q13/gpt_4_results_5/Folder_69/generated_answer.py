
def find_second_largest_num(num_list):
    if len(num_list) < 36:
        return None
    else:
        sorted_nums = sorted(num_list[32:36], reverse=True)
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
