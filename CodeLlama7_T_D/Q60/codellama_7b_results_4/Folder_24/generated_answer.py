
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, checking if each number is a left-and-right-truncatable prime number
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

def is_prime(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return False

    # Check if n is an odd number greater than 1
    if n % 2 == 0 or n <= 1:
        return False

    # Start checking if n is divisible by any number between 3 and the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    # If none of the numbers between 3 and the square root of n divide n, then n is a prime number
    return True

def is_left_right_truncatable_prime(n):
    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the leading leftmost digit of n is not equal to 1
    if str(n)[0] == '1':
        return False

    # Check if the last rightmost digit of n is not equal to 1
    if str(n)[-1] == '1':
        return False

    # If none of the above conditions are met, then n is a left-and-right-truncatable prime number
    return True
