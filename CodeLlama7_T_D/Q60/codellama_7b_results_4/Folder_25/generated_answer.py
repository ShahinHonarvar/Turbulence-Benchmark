
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Check if x is a prime number and add it to the list if it is
    if is_prime(x):
        prime_numbers.append(x)

    # Iterate from 10 to x, checking if each number is a left-and-right-truncatable prime number
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in ascending order
    return sorted(prime_numbers)
