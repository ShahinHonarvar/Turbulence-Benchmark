
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

# Check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and n - 1, it is a prime number
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains 0
    if '0' in str(n):
        return False

    # Check if the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, len(str(n)))):
        # Calculate the number obtained by removing the leftmost digit
        left_number = n % 10 ** (len(str(n))) - 10 ** (i - 1)
        # Check if the left_number is a prime number
        if not is_prime(left_number):
            return False

    # If all the checks are passed, the number is a left-and-right-truncatable prime number
    return True
