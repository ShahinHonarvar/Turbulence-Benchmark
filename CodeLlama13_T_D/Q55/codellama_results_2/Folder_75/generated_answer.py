
def lists_with_product_equal_n(circular_list, n):
    # initialize an empty list to store the results
    result = []
    
    # loop through each sublist of length i in the circular list
    for i in range(1, len(circular_list)):
        # loop through each combination of sublists of length i in the circular list
        for j in itertools.combinations(circular_list, i):
            # check if the product of the elements in the current sublist is equal to n
            if np.prod(j) == n:
                # if it is, add the sublist to the result list
                result.append(list(j))
    
    # return the result list
    return result
