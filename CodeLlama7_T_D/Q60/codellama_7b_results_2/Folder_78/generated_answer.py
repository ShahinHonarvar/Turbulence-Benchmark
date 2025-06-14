 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    # Loop through all numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)
    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # If the loop completes without returning False, return True
    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            # Remove the leading leftmost digit of i from n and check if the result is a prime number
            if is_prime(n // 10 ** (len(str(i))) - 1)):
                # Check if the last rightmost digit of i is simultaneously successively removed down to a one- or two-digit prime
                if is_prime(i % 10) and is_prime(i // 10)):
                    # Return True if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
                    return True

    # If the loop completes without returning True, return False
    return False
