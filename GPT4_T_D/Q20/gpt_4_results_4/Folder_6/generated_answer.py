
def find_n_th_smallest_num(num_list):
    num_list_slice = num_list[15:25]
    num_list_slice.sort()
    return num_list_slice[6]
