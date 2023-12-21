
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    # initialize an empty list to store the results
    result = []
    
    # iterate over the tuple of positive integers
    for i in tuple_of_positive_integers:
        # check if the current integer is a left-and-right-truncatable prime number
        if is_left_and_right_truncatable_prime(i):
            # add the current integer to the result list
            result.append(i)
    
    # sort the result list in descending order
    result.sort(reverse=True)
    
    # return the sorted result list
    return result
