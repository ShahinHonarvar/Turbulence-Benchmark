
def find_n_th_smallest_num(my_list):
    n = 7
    start, end = 23, 45
    
    # create a sub-list of the relevant indices
    subset = my_list[start:end+1]
    
    # sort the sub-list
    sorted_subset = sorted(subset)
    
    # return the nth smallest number from the sorted sub-list
    return sorted_subset[n-1]
