
def find_second_largest_num(num_list):
    sort_list = sorted(num_list[:5])
    if len(sort_list) < 2:
        return None
    else:
        return sort_list[-2]
