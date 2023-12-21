
def find_n_th_smallest_num(my_list):
    n = 6
    start_index = 55
    end_index = 66
    
    return sorted(my_list)[start_index:end_index][n-1]
