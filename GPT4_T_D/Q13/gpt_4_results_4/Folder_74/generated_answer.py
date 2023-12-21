
def find_second_largest_num(num_list):
    if len(num_list) >= 78:
        sorted_list = sorted(num_list[17:79])
        return sorted_list[-2]
    else:
        return None
