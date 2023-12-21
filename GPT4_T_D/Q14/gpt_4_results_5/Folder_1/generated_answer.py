
def find_second_smallest_num(nums_list):
    if len(nums_list) < 35:
        return None
    else:
        sorted_nums = sorted(nums_list[34:56])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
