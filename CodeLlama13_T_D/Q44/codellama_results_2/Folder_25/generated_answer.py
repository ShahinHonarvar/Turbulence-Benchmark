
def composite_nums_between_indices(num_list):
    # find the indices of 75 and 94 in the list
    ind_75 = num_list.index(75)
    ind_94 = num_list.index(94)
    
    # get the slice of the list between those indices, inclusive
    composite_slice = num_list[ind_75:ind_94+1]
    
    # return the set of all composite numbers in that slice
    return {num for num in composite_slice if is_composite(num)}
