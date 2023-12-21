
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple of positive integers
    for i in range(len(tuple)):
        x = tuple[i]

        # Check if x is a prime number
        if is_prime(x):
            # Add x to the list of prime numbers
            prime_numbers.append(x)

        # Check if any right-truncatable prime numbers exist less than x
        for j in range(len(prime_numbers)):
            y = prime_numbers[j]

            # Check if y is a right-truncatable prime number
            if is_right_truncatable_prime(y):
                # Add y to the list of prime numbers
                prime_numbers.append(y)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers, key=lambda x: int(str(x)[:-1]))

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the value of n % 2
        i = n % 2

        # Iterate from 3 to the square root of n
        for j in range(3, int(n ** 0.5) + 1, 2):
            # Check if j divides n without a remainder
            if (n % j) == 0:
                # Return False if any such j is found
                return False

        # If no such j is found, return True
        return True

# Function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if is_prime(n):
        # Initialize a variable to store the value of n % 10
        i = n % 10

        # Iterate from n-1 to 1
        for j in range(n-1, -1, -1):
            # Check if the last digit of j is less than or equal to the last digit of n
            if j % 10 <= i:
                # Return False if any such j is found
                return False

        # If no such j is found, return True
        return True
