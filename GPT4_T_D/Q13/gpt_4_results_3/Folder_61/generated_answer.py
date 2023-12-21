
def find_second_largest_num(num_list):
    sorted_nums = sorted(num_list[0:8], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
