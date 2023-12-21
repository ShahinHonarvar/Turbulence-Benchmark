
def find_n_th_smallest_num(num_list):
    if len(num_list) < 80:
        return 'Input list is too short'
    else:
        return sorted(num_list[63:80])[10]
