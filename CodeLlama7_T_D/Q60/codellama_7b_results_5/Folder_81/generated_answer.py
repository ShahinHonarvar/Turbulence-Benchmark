
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

    # Sort the list in ascending order
    prime_numbers = sorted(prime_numbers)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # If the number is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number makes it this far, it is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Convert the number to a string
    s = str(n)

    # Check if the number contains any 0 digits
    for c in s:
        if c == '0':
            return False

    # Check if the number is a palindrome
    if s == s[::-1]:

        # Check if the number remains prime after removing the leading leftmost and last rightmost digits
        for i in range(len(s) - 1):
            if not is_prime(int(s[i + 1:])))
                return False

    # If the number makes it this far, it is a left-and-right-truncatable prime number
    return True
