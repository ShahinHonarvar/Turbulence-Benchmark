
def find_second_largest_num(num_list):
    range_list = num_list[15:40]
    if len(range_list) < 2:
        return None
    else:
        range_list.sort()
        return range_list[-2]
