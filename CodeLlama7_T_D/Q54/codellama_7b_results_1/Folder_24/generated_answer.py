
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    for i in range(2, x):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is right-truncatable prime
            if is_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    return prime_numbers
