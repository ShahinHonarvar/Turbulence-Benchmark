
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

# Check if a number is a prime number
def is_prime(n):
    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of the number, it is prime
    return True

# Check if a number is left-and-right-truncatable
def is_left_right_truncatable(n):
    # Get the length of the number in digits
    num_length = len(str(n))

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        # If the number is divisible by any number between 2 and the square root of the number, it is not left-and-right-truncatable
        if n % i == 0:
            return False

    # Check if the number contains the digit "0"
    for digit in str(n):
        if digit == "0":
            return False

    # If the number is not divisible by any number between 2 and the square root of the number, it does not contain the digit "0", and the length of the number in digits is greater than or equal to 3, it is left-and-right-truncatable
    return num_length >= 3
