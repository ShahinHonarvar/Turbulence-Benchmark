
def find_second_largest_num(num_list):
    short_list = num_list[:3]
    if len(short_list) < 2:
        return None
    else:
        short_list.sort()
        return short_list[-2]
