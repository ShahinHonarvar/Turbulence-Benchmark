
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers

def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if n contains no 0
    if "0" in str(n):
        return False

    # Create a copy of n
    num = n

    # Remove the leading leftmost and last rightmost digits of n
    while num > 9:
        num = int(str(num)[:-1])

    # Check if the remaining number is prime
    return is_prime(num)
