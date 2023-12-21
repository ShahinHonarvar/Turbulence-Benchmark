
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # If the current number is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If the current number is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        # If the number is less than or equal to 1, return False
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1)):
        # If the number is divisible by any number between 2 and the square root of the number, return False
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of the number, return True
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digits
    if '0' in str(n):
        # If the number contains any 0 digits, return False
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        # If the number is not a prime number, return False
        return False

    # Check if the leading leftmost and last rightmost digits of the number are simultaneously successively removed down to a one- or two-digit prime
    for i in range(2, len(str(n)))):
        # If the leading leftmost and last rightmost digits of the number are simultaneously successively removed down to a one- or two-digit prime, return True
        if is_prime(int(str(n)[i:] + str(n)[:i]))):
            return True

    # If the leading leftmost and last rightmost digits of the number are not simultaneously successively removed down to a one- or two-digit prime, return False
    return False
