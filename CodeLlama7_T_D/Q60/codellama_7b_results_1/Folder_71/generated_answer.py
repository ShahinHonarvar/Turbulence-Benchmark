
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers (in descending order)
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime or not
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of n, it is prime
    return True

# Check if a number is left-and-right-truncatable prime or not
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digit
    if '0' in str(n):
        return False

    # Check if the number is a palindrome (i.e., it reads the same forward and backward)
    if str(n) == str(n)[::-1]:
        return True

    # If the number is not a palindrome, check if it is left-and-right-truncatable prime by removing the leading leftmost and last rightmost digits one at a time until the resulting numbers are either 1 or 2 digits long
    while len(str(n)) > 2:
        # Remove the leading leftmost digit of the number
        n = int(str(n)[1:]))
        # Check if the resulting number is prime
        if is_prime(n):
            return True

    # If the number is not a palindrome and none of its digits can be removed to make it left-and-right-truncatable prime, it is not a left-and-right-truncatable prime
    return False
