
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):

            # Check if i divides n
            if n % i == 0:

                # Return False if a prime factor is found
                return False

    # Return True if n is a prime number
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains 0
    if '0' in str(n):

        # Return False if the number contains 0
        return False

    # Iterate from the leading leftmost digit to the last rightmost digit of n
    for i in range(len(str(n)))):

        # Check if the number is not prime after removing the leading leftmost and last rightmost digits
        if not is_prime(int(str(n)[:i] + str(n)[i+1:])))

            # Return False if the number is not prime after removing the leading leftmost and last rightmost digits
            return False

    # Return True if the number is a left-and-right-truncatable prime number
    return True
