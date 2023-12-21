
def find_n_th_smallest_num(num_list):
    if len(num_list) < 6:
        return 'The list has less than 6 elements'
    else:
        num_list.sort()
        return num_list[5]
