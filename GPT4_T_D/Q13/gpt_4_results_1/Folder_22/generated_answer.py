
def find_second_largest_num(num_list):
    filter_list = num_list[40:201]
    if not filter_list:
        return None
    filter_list.sort()
    return filter_list[-2] if len(filter_list) > 1 else None
