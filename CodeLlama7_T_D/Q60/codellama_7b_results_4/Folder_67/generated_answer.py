
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    
    # Iterate through the range of values from 1 to x
    for i in range(1, x + 1):
        
        # Check if the current value is a prime number
        if is_prime(i):
            
            # If the current value is a prime number, check if it is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                
                # If the current value is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)
    
    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)
