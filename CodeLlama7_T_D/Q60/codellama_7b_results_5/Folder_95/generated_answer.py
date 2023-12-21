
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    return prime_numbers
