
def all_left_truncatable_prime(tuple_of_positive_integers):
    # Initialize an empty list to store the left-truncatable prime numbers
    left_truncatable_prime_numbers = []
    
    # Iterate over the tuple of positive integers
    for i in range(len(tuple_of_positive_integers)):
        
        # Get the current integer from the tuple
        current_integer = tuple_of_positive_integers[i]
        
        # Check if the current integer is a prime number
        if is_prime(current_integer):
            
            # Initialize an empty string to store the left-truncated version of the current integer
            left_truncated_string = ""
            
            # Iterate over the digits of the current integer in reverse order
            for j in range(len(str(current_integer))) - 1, -1:
                
                # Get the current digit from the string representation of the current integer
                current_digit = str(current_integer)[j]
                
                # Check if the current digit is a 0
                if current_digit == "0":
                    
                    # Skip to the next iteration of the loop
                    continue
                
                
                # Add the current digit to the left-truncated string
                left_truncated_string += current_digit
            
            
            # Check if the left-truncated string is an empty string
            if len(left_truncated_string) == 0:
                
                # Add the current integer to the list of left-truncatable prime numbers
                left_truncatable_prime_numbers.append(current_integer)
            
            
            # Check if the left-truncated string is a single digit
            elif len(left_truncated_string) == 1:
                
                # Check if the single digit is a prime number
                if is_prime(int(left_truncated_string)):
                    
                    # Add the current integer to the list of left-truncatable prime numbers
                    left_truncatable_prime_numbers.append(current_integer)
            
            
            # Check if the left-truncated string is a multiple digit number
            else:
                
                # Check if the multiple digit number is a prime number
                if is_prime(int(left_truncated_string)):
                    
                    # Add the current integer to the list of left-truncatable prime numbers
                    left_truncatable_prime_numbers.append(current_integer)
        
        
        # Check if the current integer is a composite number
        elif not is_prime(current_integer):
            
            # Skip to the next iteration of the loop
            continue
    
    
    # Sort the list of left-truncatable prime numbers in ascending order
    left_truncatable_prime_numbers.sort()
    
    # Return the sorted list of left-truncatable prime numbers
    return left_truncatable_prime_numbers
