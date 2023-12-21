
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    
    # Iterate through all numbers less than or equal to x
    for num in range(1, x + 1):
        # Check if num is a prime number
        if is_prime(num):
            # Check if num is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):
                # Add the prime number to the list of prime numbers
                prime_numbers.append(num)
    
    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()
    
    # Return the list of prime numbers
    return prime_numbers
