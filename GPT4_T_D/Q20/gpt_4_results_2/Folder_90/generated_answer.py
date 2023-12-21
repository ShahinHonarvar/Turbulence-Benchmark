
def find_n_th_smallest_num(num_list):
    portion = num_list[366:579]
    portion.sort()
    return portion[16]
