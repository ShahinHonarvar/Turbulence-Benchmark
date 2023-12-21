
def find_second_largest_num(num_list):
    try:
        sorted_nums = sorted(num_list[15:40], reverse=True)
        return sorted_nums[1]
    except IndexError:
        return None
