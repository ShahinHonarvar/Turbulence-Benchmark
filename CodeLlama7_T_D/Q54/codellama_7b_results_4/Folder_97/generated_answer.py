
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through each number in the tuple
    for i in range(len(tuple)):
        x = tuple[i]

        # Check if the number is a prime number
        if is_prime(x):

            # Check if the number is right-truncatable
            if is_right_truncatable(x):

                # Add the prime number to the list
                prime_numbers.append(x)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is prime
def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the number is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number makes it through all the checks, it must be prime
    return True

# Check if a right-truncatable prime number is still prime after removing its last rightmost digit
def is_right_truncatable(n):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through each number in the tuple
    for i in range(len(tuple)):
        x = tuple[i]

        # Check if the number is a prime number
        if is_prime(x):

            # Check if the number is right-truncatable
            if is_right_truncatable(x):

                # Add the prime number to the list
                prime_numbers.append(x)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers
