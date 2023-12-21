
def find_n_th_smallest_num(num_list):
    slice_list = num_list[106:255]
    sorted_list = sorted(slice_list)
    return sorted_list[8]
