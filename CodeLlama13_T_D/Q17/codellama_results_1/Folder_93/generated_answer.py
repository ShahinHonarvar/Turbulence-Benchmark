
def all_ints_div_by_both_two_nums(my_list):
    # find the indices of elements divisible by -61 and -79
    indices = []
    for i, x in enumerate(my_list):
        if x % -61 == 0 and x % -79 == 0:
            indices.append(i)
    
    # return the list of elements at those indices
    return [my_list[i] for i in indices]
