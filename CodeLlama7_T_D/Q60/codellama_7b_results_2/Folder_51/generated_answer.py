
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)
    return prime_numbers

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not a prime number
                return False
    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is a prime number
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, then it cannot be a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are all different
    for i in range(len(str(n)))):
        # Check if the current digit is equal to the previous digit
        if str(n)[i] == str(n)[i - 1]:
            # If the current digit is equal to the previous digit, then n cannot be a left-and-right-truncatable prime number
            return False

    # Check if the leading leftmost and last rightmost digits of n are all different
    for i in range(len(str(n)))):
        # Check if the current digit is equal to the previous digit
        if str(n)[i] == str(n)[i - 1]:
            # If the current digit is equal to the previous digit, then n cannot be a left-and-right-truncatable prime number
            return False

    # If all of the above conditions are met, then n is a left-and-right-truncatable prime number
    return True
