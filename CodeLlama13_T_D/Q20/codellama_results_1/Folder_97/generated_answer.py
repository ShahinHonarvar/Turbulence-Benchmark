
def find_n_th_smallest_num(my_list):
    n = 15
    start, end = 60, 83
    
    return sorted(my_list[start:end+1])[n-1]
