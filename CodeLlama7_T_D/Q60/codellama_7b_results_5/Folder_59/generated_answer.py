
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If i is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is equal to 1 or less than 2
    if n == 1 or n < 2:
        # Return False if the condition is met
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by any number between 2 and sqrt(n), return False
        if n % i == 0:
            return False

    # Return True if the condition is not met
    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is equal to 1 or less than 2
    if n == 1 or n < 2:
        # Return False if the condition is met
        return False

    # Check if n contains any digit other than 0 and 1
    for i in range(len(str(n)))):
        # If n contains any digit other than 0 and 1, return False
        if str(n)[i] != "0" and str(n)[i] != "1":
            return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(len(str(n)))):
        # If the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number, return True
        if is_prime(int(str(n)[i:] + str(n)[:i]))) == True:
            return True

    # Return False if the condition is not met
    return False
