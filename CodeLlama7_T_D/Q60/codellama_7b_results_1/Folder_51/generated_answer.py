
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Check if x is a prime number and add it to the list of prime numbers if it is
    if is_prime(x) and has_no_zeros(x):
        prime_numbers.append(x)

    # Iterate over all numbers less than or equal to x
    for i in range(1, x + 1):

        # Check if the number is a left-and-right-truncatable prime number and add it to the list of prime numbers if it is
        if is_left_right_truncatable_prime(i) and has_no_zeros(i):
            prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers
