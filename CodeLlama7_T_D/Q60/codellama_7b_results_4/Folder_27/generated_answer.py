
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the range of integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current integer to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    return prime_numbers
