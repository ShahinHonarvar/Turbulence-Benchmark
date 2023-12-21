
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through each integer in the tuple
    for i in range(len(tuple_of_positive_integers)):
        # Check if the current integer is a left-and-right-truncatable prime
        if is_left_right_truncatable_prime(i):
            # If it is, add it to the result list
            result.append(i)
    
    # Sort the result list in descending order
    result.sort(reverse=True)
    
    # Return the sorted result list
    return result
