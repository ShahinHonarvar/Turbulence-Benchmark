
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # If it is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If it is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If it does, return False
                return False

    # If we reach this point, n is prime
    return True

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If it is not a prime number, return False
        return False

    # Check if the leading leftmost digit of n is 1
    if str(n)[0] != '1':
        # If the leading leftmost digit of n is not 1, return False
        return False

    # Check if the last rightmost digit of n is a prime number
    if not is_prime(int(str(n)[-1]))):
        # If the last rightmost digit of n is not a prime number, return False
        return False

    # If we reach this point, n is a left-and-right-truncatable prime number
    return True
