 def all_left_right_truncatable_prime(x):
    # Initialize the list of left-and-right-truncatable prime numbers
    left_right_truncatable_primes = []
    # Iterate through the range of positive integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current integer to the list of left-and-right-truncatable prime numbers
                left_right_truncatable_primes.append(i)
    # Return the sorted list of left-and-right-truncatable prime numbers
    return sorted(left_right_truncatable_primes)
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize the factorization of n to 1
        factorization = 1
        # Iterate through the range of positive integers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i is a factor of n
            if n % i == 0:
                # Update the factorization of n
                factorization = i * factorization
                # Break out of the loop since we have found a factor of n
                break

    # Return True if n has a prime factorization and False otherwise
    return factorization == n

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False since n is not a prime number
        return False

    # Initialize the string representation of n to the empty string
    n_str = ""

    # Iterate through the digits of n in reverse order
    for digit in str(n)[::-1]:
        # Add the current digit to the string representation of n
        n_str += digit

    # Initialize a list to store the prime factors of n
    prime_factors = []

    # Iterate through the digits of n_str in reverse order
    for digit in str(n_str)[::-1]:
        # Check if the current digit is not equal to 0 and is less than or equal to 9
        if digit != "0" and int(digit) <= 9:
            # Add the current digit to the list of prime factors of n
            prime_factors.append(int(digit))

    # Check if the sum of the prime factors of n is equal to n
    if sum(prime_factors) == n:
        # Return True since the sum of the prime factors of n is equal to n and n is a left-and-right-truncatable prime number
        return True

    # Return False since the sum of the prime factors of n is not equal to n and n is not a left-and-right-truncatable prime number
    return False
