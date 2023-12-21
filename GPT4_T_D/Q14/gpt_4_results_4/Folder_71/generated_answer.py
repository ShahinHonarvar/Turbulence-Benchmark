
def find_second_smallest_num(num_list):
    if len(num_list) < 31: 
        return None
    sorted_nums = sorted(num_list[29:52])
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None
