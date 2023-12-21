
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for i in tuple:

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is right-truncatable
            if is_right_truncatable(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

        # If the number is not divisible by 2 to n-1, it is prime
        return True

# Check if a number is right-truncatable
def is_right_truncatable(n):
    # Check if n is greater than or equal to 10
    if n >= 10:

        # Check if the last digit of n is prime
        if is_prime(int(str(n)[-1]))):

            # Check if n can be divided by the number formed by removing its last rightmost digit
            if n % int(str(n)[-2:-1]) == 0:

                # Return True if the number is right-truncatable
                return True

    # Return False if the number is not right-truncatable
    return False
