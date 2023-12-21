
def find_n_th_smallest_num(num_list):
    num_list.sort()
    try:
        return num_list[7]
    except IndexError:
        return "List is too short"
