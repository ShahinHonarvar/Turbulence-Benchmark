
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # If it is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):
                # If it is left-and-right-truncatable, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If none of the above conditions are met, then n is a prime number
    return True

# Function to check if a number is left-and-right-truncatable
def is_left_right_truncatable(n):
    # Initialize two variables to store the leading and last digits of n
    leading = 0
    last = 0

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Get the leading and last digits of n
    leading = int(str(n)[0]))
    last = int(str(n)[-1]))

    # Check if the leading and last digits are both prime numbers
    if is_prime(leading) and is_prime(last):
        return True

    # If the leading and last digits are not both prime numbers, then n is not left-and-right-truncatable
    return False
