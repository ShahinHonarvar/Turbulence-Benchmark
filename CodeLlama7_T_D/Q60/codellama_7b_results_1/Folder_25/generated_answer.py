
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by any number between 2 and the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is prime
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading digit of n is 1 or 2
    if n // 10 ** (len(str(n))) - 1) != 1 and n % 2 != 0:
        return False

    # Check if the trailing digit of n is 1 or 3
    if n % 10 ** (len(str(n))) - 1) != 1 and n % 3 != 0:
        return False

    # If all the above conditions are met, then n is a left-and-right-truncatable prime number
    return True
