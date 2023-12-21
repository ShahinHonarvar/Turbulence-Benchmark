
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and n - 1, it is prime
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n contains a zero digit
    if '0' in str(n):
        return False

    # Check if n is divisible by its leading leftmost digit
    if int(str(n)[0])) != 0 and n % int(str(n)[0])) != 0:
        return False

    # Check if n is divisible by its last rightmost digit
    if int(str(n)[-1]))) != 0 and n % int(str(n)[-1]))) != 0:
        return False

    # If the number does not contain a zero digit, it is not divisible by any number between its leading leftmost digit and its last rightmost digit, and it remains prime if these digits are simultaneously successively removed down to a one- or two-digit prime.
    return True
