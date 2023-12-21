
def find_n_th_smallest_num(number_list):
    number_list_range = number_list[299:636]
    number_list_range.sort()
    return number_list_range[11]
