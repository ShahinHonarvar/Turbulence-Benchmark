
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of prime numbers in sorted order
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the value of n % 2
        i = n % 2
        # Iterate from 3 to the square root of n (both inclusive)
        for j in range(3, int(n ** 0.5) + 1, 2):
            # Check if j divides n without leaving a remainder
            if i == 0:
                break
            else:
                i = n % j

    # Return True if n is a prime number and False otherwise
    return i == 0

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if is_prime(n):
        # Initialize variables to store the value of n % 10 and n // 10
        i = n % 10
        j = n // 10

        # Iterate from 2 to the square root of n (both inclusive)
        for k in range(2, int(n ** 0.5) + 1):
            # Check if k divides n without leaving a remainder
            if i == 0 and j == 0:
                break
            else:
                i = n % k
                j = n // k

    # Return True if n is a left-and-right-truncatable prime number and False otherwise
    return i == 0 and j == 0
