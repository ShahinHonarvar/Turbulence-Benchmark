
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-truncatable
            if is_left_truncatable(i):

                # Add the number to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list)

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is 1 or less than 2
    if n <= 1:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number makes it through all the checks, it is prime
    return True

# Check if a number is left-truncatable
def is_left_truncatable(n):
    # Get the length of the number in base 10
    num_len = len(str(n))

    # Iterate from 2 to the length of the number
    for i in range(2, num_len + 1):

        # Get the leftmost digit of the number
        leftmost_digit = int(str(n)[0:i])

        # Check if the number is prime after removing the leftmost digit
        if is_prime(n // 10 ** (i - 1)) and leftmost_digit != 0:

            # If the number makes it through all the checks, it is left-truncatable
            return True

    # If the number does not make it through all the checks, it is not left-truncatable
    return False
