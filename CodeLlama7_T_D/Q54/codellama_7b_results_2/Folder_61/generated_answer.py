
def all_right_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the right-truncatable prime numbers
    list_of_rtsps = []
    
    # Iterate through each integer in the tuple
    for i in range(len(tuple_of_integers)):
        
        # Get the current integer from the tuple
        x = tuple_of_integers[i]
        
        # Check if x is a prime number
        if is_prime(x):
            
            # Initialize an empty string to store the rightmost digit of x
            last_digit = ''
            
            # Iterate through each digit in the representation of x as a string
            for j in range(len(str(x)))):
                
                # Get the current digit from the representation of x as a string
                digit = str(x)[j]
                
                # Check if the current digit is equal to the last rightmost digit of x
                if digit == last_digit:
                    
                    # Remove the last rightmost digit of x and check if it remains prime
                    y = int(str(x)[:-1]))
                    if is_prime(y):
                        
                        # Add y to the list of right-truncatable prime numbers
                        list_of_rtsps.append(y)
            
            # Sort the list of right-truncatable prime numbers in descending order
            list_of_rtsps.sort(reverse=True)
            
            # Return the sorted list of right-truncatable prime numbers
            return list_of_rtsps
        
        # If x is not a prime number, continue to the next integer in the tuple
    
    # If there are no right-truncatable prime numbers less than x, return an empty list
    return []
