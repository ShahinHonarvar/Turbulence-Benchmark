
def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all numbers less than n
    for i in range(2, n):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is right-truncatable prime number
            if is_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list, reverse=True)

# Check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is greater than 1
    return True

# Check if a number is right-truncatable prime number
def is_right_truncatable_prime(n):

    # Loop through all numbers less than or equal to the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        # Check if i divides n
        if n % i == 0:

            # Return False if i divides n
            return False

    # Return True if n is greater than 1
    return True
