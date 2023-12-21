
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Check if x is a prime number
    if is_prime(x):
        # If x is a prime number, add it to the list of prime numbers
        prime_numbers.append(x)

    # Loop through all the prime numbers less than or equal to x
    for i in range(2, int(math.sqrt(x)) + 1)):
        # Check if i is a left-and-right-truncatable prime number
        if is_left_right_truncatable_prime(i):
            # If i is a left-and-right-truncatable prime number, add it to the list of prime numbers
            prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers)
