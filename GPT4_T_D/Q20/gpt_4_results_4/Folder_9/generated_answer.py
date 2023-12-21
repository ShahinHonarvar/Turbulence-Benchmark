
def find_n_th_smallest_num(num_list):
    num_list = num_list[10:101]
    num_list.sort()
    return num_list[9]
