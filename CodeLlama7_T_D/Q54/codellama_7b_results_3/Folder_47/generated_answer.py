
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than x
    for num in range(1, x):

        # Check if num is a prime number
        if is_prime(num):

            # Check if num is right-truncatable prime number
            if is_right_truncatable_prime(num):

                # Add num to the list of prime numbers
                prime_numbers.append(num)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all odd numbers up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n without a remainder
            if n % i == 0:

                # Return False if i divides n without a remainder
                return False

    # Return True if n is greater than 1 and has no factors other than itself and 1
    return True

# Function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # Return False if n is not a prime number
        return False

    # Loop through all digits of n in reverse order
    for digit in str(n)[::-1]:

        # Check if the digit can be removed without making n non-prime
        if not is_prime(int(str(n)[:-len(digit)] + str(digit)[:-1]))) and len(digit) > 1:

            # Return False if the digit cannot be removed without making n non-prime
            return False

    # Return True if all digits of n can be removed without making n non-prime
    return True
