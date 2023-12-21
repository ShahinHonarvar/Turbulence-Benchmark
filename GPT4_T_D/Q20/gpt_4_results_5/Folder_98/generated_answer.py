
def find_n_th_smallest_num(num_list):
    if len(num_list) >= 9:
        num_list.sort()
        return num_list[8]
    else:
        return 'The list should contain at least 9 elements'
