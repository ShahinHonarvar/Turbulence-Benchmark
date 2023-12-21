
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over the range of numbers from 1 to x
    for i in range(1, x + 1):
        
        # Check if the current number is a prime number
        if is_prime(i):
            
            # Check if the current number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                
                # Add the current number to the results list
                results.append(i)
    
    # Sort the results list in ascending order
    results.sort()
    
    # Return the sorted results list
    return results
