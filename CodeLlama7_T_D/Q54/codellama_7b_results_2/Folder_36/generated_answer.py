 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    right_truncatable_primes = []
    # Iterate through the tuple of positive integers
    for x in tuple:
        # Check if x is a prime number
        if is_prime(x):
            # Initialize an empty string to store the last rightmost digit of x
            last_digit = ""
            # Keep removing the last rightmost digit of x until it becomes a prime number
            while not is_prime(x):
                # Remove the last rightmost digit of x and store it in last_digit
                last_digit = str(x % 10)
                x = int(str(x // 10))
            # Add x to the list of right-truncatable prime numbers if it is a prime number
            if is_prime(x):
                right_truncatable_primes.append(x)
    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(right_truncatable_primes)
# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if a prime factor is found
                return False

    # Return True if n is a prime number
    return True
