
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for i in range(len(tuple)):

        # Check if the current integer is a prime number
        if is_prime(tuple[i]):

            # If the current integer is a prime number, append it to the list of prime numbers
            prime_numbers.append(tuple[i])

    # Initialize an empty string to store the right-truncatable prime numbers
    right_truncatable_prime_numbers = ''

    # Loop through each prime number in the list
    for i in range(len(prime_numbers)):

        # Check if the current prime number is a right-truncatable prime number
        if is_right_truncatable_prime(prime_numbers[i]):

            # If the current prime number is a right-truncatable prime number, append it to the list of right-truncatable prime numbers
            right_truncatable_prime_numbers += str(prime_numbers[i]) + ' '

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(right_truncatable_prime_numbers.split())

# Define a function to check if an integer is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the odd numbers less than or equal to the square root of n
        for i in range(3, int(n ** 0.5) + 1, 2):

            # Check if i divides n
            if n % i == 0:

                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any odd number less than or equal to its square root, it is prime
    return True

# Define a function to check if an integer is a right-truncatable prime number
def is_right_truncatable_prime(n):

    # Initialize a variable to store the last rightmost digit of n
    last_digit = n % 10

    # Check if n is divisible by the last rightmost digit of n
    if n % last_digit == 0:

        # If n is divisible by the last rightmost digit of n, return False
        return False

    # Loop through all the prime factors of n
    for i in range(len(prime_factors)):

        # Check if the current prime factor is equal to the last rightmost digit of n
        if prime_factors[i] == last_digit:

            # If the current prime factor is equal to the last rightmost digit of n, return True
            return True

    # If n is not divisible by any prime factor less than or equal to its square root, it is a right-truncatable prime number
    return False
