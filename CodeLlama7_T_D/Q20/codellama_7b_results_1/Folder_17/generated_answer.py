
def find_n_th_smallest_num(my_list):
    # Find the index of the 7th smallest number
    n = 7
    my_list.sort()
    for i in range(len(my_list)):
        if i == (n-1):
            return my_list[i]
