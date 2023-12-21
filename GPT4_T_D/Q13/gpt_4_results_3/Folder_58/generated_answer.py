
def find_second_largest_num(num_list):
    if len(num_list)<557:
        return None
    sorted_list = sorted(num_list[209:557])
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[-2]
