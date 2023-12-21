
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the range of integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # If it is, check if it is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # If it is, add it to the list of prime numbers
                prime_numbers.append(i)
    # Sort the list of prime numbers in ascending order
    prime_numbers = sorted(prime_numbers)
    # Return the list of prime numbers
    return prime_numbers
