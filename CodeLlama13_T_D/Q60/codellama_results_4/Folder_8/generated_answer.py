
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    left_right_truncatable_primes = []
    
    # Iterate over the tuple of positive integers
    for i in range(len(tuple_of_positive_integers)):
        # Get the current integer and its string representation
        current_integer = tuple_of_positive_integers[i]
        current_string = str(current_integer)
        
        # Check if the current integer is a left-and-right-truncatable prime number
        if all_left_right_truncatable_prime_helper(current_string):
            # If it is, add it to the list of left-and-right-truncatable prime numbers
            left_right_truncatable_primes.append(current_integer)
    
    # Sort the list of left-and-right-truncatable prime numbers in descending order
    left_right_truncatable_primes.sort(reverse=True)
    
    # Return the list of left-and-right-truncatable prime numbers
    return left_right_truncatable_primes
