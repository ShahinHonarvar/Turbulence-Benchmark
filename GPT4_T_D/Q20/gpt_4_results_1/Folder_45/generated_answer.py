
def find_n_th_smallest_num(input_list):
    if len(input_list)<16:
        return "There are less than 16 elements in the input list"
    else:
        input_list.sort()
        return input_list[15]
