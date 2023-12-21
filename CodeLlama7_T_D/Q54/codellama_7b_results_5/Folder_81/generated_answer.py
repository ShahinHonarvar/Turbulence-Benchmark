
def all_right_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for integer in tuple_of_integers:
        if is_prime(integer):
            # If the integer is a prime number, check if it is right-truncatable
            if is_right_truncatable(integer):
                # If the integer is both a prime number and a right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(integer)
    return sorted(prime_numbers)

# Function to check if an integer is a prime number
def is_prime(n):
    # Check if n is less than 2 or not an integer
    if n < 2 or not isinstance(n, int):
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    return True

# Function to check if an integer is a right-truncatable prime number
def is_right_truncatable(n):
    # Check if n is less than 2 or not an integer
    if n < 2 or not isinstance(n, int):
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    # Check if the last digit of n is a prime number
    if not is_prime(int(str(n)[-1]))):
        return False

    return True
