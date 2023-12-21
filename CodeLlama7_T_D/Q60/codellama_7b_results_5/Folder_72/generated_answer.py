
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)
    return prime_numbers
