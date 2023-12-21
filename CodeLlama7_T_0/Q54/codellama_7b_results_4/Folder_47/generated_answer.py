
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for i in range(49):
        # Check if the current number is a prime number
        if is_prime(tuple[i]):
            # If it is, add it to the list of prime numbers
            prime_numbers.append(tuple[i])

    # Iterate over the list of prime numbers and check if they are right-truncatable prime numbers
    for i in range(len(prime_numbers)):
        # Check if the current number is a right-truncatable prime number
        if is_right_truncatable_prime(prime_numbers[i]):
            # If it is, add it to the list of right-truncatable prime numbers
            right_truncatable_prime_numbers.append(prime_numbers[i])

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(right_truncatable_prime_numbers)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If it does, return False
                return False

    # If we reach this point, either n is a prime number or it is not a prime number
    return True

# Define a function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if is_prime(n):
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If it does, return False
                return False

    # If we reach this point, either n is a right-truncatable prime number or it is not a right-truncatable prime number
    return True
