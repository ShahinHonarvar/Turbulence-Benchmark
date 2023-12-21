
def find_second_largest_num(num_list):
    if len(num_list) < 3:
        return None
    else:
        sorted_list = sorted(num_list[0:3])
        return sorted_list[-2]
