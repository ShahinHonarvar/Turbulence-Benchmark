
def all_left_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[52]
    prime_list = []
    # Loop through all numbers less than x
    for i in range(1, x):
        # Check if number is prime
        if is_prime(i):
            # Check if number is left-truncatable prime
            if is_left_truncatable_prime(i):
                # Add number to list of prime numbers
                prime_list.append(i)
    # Sort list of prime numbers in descending order
    prime_list.sort(reverse=True)
    return prime_list

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                # Return False since n is not prime
                return False

    # Return True since n is prime
    return True

def is_left_truncatable_prime(n):
    # Check if n contains any 0 digits
    if '0' in str(n):
        # Return False since n contains a 0 digit
        return False

    # Loop through all numbers less than or equal to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n without leaving a remainder
        if n % i == 0:
            # Return False since n is not left-truncatable prime
            return False

    # Return True since n is left-truncatable prime
    return True
