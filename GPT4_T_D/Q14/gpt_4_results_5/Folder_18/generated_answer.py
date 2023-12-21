
def find_second_smallest_num(num_list):
    if len(num_list) < 49:
        return None
    else:
        sorted_nums = sorted(num_list[30:49])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
        else:
            return None
