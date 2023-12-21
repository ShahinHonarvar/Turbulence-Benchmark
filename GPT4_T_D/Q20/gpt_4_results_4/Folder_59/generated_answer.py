
def find_n_th_smallest_num(num_list):
    num_list.sort()
    try:
        return num_list[11]
    except IndexError:
        return 'List has less than 12 items'
