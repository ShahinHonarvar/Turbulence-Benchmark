
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_list.append(i)

    # Sort the list in descending order
    prime_list = sorted(prime_list, reverse=True)

    # Return the list of left-and-right-truncatable prime numbers less than or equal to x
    return prime_list

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, return False
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(10):
        # Check if the digit i is the leading leftmost digit of n
        if str(i) == n[0]:
            # If the digit i is the leading leftmost digit of n, check if it is also the last rightmost digit of n
            if str(i) == n[-1]:
                # If the digit i is both the leading leftmost digit of n and the last rightmost digit of n, return True
                return True

    # If none of the digits in the range 0 to 9 are simultaneously successively removed down to a one- or two-digit prime, return False
    return False
