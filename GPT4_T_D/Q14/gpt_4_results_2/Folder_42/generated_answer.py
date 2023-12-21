
def find_second_smallest_num(list_of_nums):
    if len(list_of_nums[21:98]) < 2:
        return None
    else:
        sorted_list = sorted(list_of_nums[21:98])
        return sorted_list[1]
