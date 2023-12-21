
def find_second_smallest_num(num_list):
    if len(num_list) < 38:
        return None
    else:
        sorted_nums = sorted(num_list[37:52])
        if len(sorted_nums) < 2:  
            return None
        else:
            return sorted_nums[1]
