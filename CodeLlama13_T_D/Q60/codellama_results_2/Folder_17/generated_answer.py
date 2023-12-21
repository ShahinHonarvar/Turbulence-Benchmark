
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    primes = []
    
    # Iterate over all positive integers less than or equal to x
    for i in range(1, x+1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer contains no 0
            if '0' not in str(i):
                # Add the current integer to the list of left-and-right-truncatable prime numbers
                primes.append(i)
    
    # Return the sorted list of left-and-right-truncatable prime numbers
    return sorted(primes, reverse=True)
