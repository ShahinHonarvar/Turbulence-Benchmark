
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Check if a given number is a prime number
def is_prime(n):

    # Check if the input number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the input number is divisible by any number between 2 and the square root of the input number
    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    # If the input number is greater than 1 and it is not divisible by any number between 2 and the square root of the input number, then it is a prime number
    return True

# Check if a given number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the input number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the input number contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the input number remains prime after the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)) - 1, 0, -1)):
        if n % int(str(n)[i]) == 0:
            return False

    # If the input number is greater than 1 and it does not contain any 0 digits and it remains prime after the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime, then it is a left-and-right-truncatable prime number
    return True
