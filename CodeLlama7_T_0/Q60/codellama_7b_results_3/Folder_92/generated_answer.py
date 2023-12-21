
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n (inclusive)
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is greater than 1
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # Return False if n is not a prime number
        return False

    # Initialize an empty string to store the digits of n
    digits = ""

    # Iterate from 1 to the length of n (inclusive)
    for i in range(1, len(str(n)) + 1):

        # Check if the leading leftmost digit of n is equal to the last rightmost digit of n
        if str(n)[0] == str(n)[-1]:

            # Remove the leading leftmost and last rightmost digits from n
            n = int(str(n)[1:-1]))

            # Check if n is a prime number
            if is_prime(n):

                # Return True if n is a prime number after removing the leading leftmost and last rightmost digits
                return True

    # Return False if no left-and-right-truncatable prime number exists in the specified range
    return False
