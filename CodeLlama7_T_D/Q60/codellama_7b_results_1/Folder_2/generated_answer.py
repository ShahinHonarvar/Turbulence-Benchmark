
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_list.append(i)

    # Sort the list in ascending order
    prime_list.sort()

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_list

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is prime
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, then it is not a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are both 1 or both 2
    if n % 10 ** (len(str(n))) - 10 ** (len(str(n))) + 1 == 1 or n % 10 ** (len(str(n))) - 10 ** (len(str(n))) + 1 == 2:
        # If the leading leftmost and last rightmost digits of n are both 1 or both 2, then n is a left-and-right-truncatable prime number
        return True

    # If the leading leftmost and last rightmost digits of n are not both 1 or both 2, then n is not a left-and-right-truncatable prime number
    return False
