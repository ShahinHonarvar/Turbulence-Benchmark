
def find_n_th_smallest_num(num_list):
    num_list = num_list[12:91]
    num_list.sort()
    try:
        return num_list[16]
    except IndexError:
        return "List doesn't have 17 numbers between index 12 and 90"
