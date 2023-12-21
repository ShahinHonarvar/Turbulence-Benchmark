
def find_second_largest_num(num_list):
    if len(num_list) < 33:
        return None
    else:
        sorted_list = sorted(num_list[28:33])
        return sorted_list[-2]
