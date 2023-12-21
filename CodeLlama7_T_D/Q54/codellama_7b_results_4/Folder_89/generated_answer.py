
def all_right_truncatable_prime(tuple):
    # Extract the integer at index 97 from the tuple
    x = tuple[97]
    # Initialize an empty list to store the sorted right-truncatable prime numbers less than x
    prime_numbers = []
    # Iterate from 2 to x - 1
    for i in range(2, x):
        # Check if i is a prime number
        if is_prime(i):
            # Check if the last rightmost digit of i is successively removed, results in a prime number
            if is_right_truncatable_prime(i):
                # Add the prime number to the list of sorted right-truncatable prime numbers less than x
                prime_numbers.append(i)
    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)
    return prime_numbers

# Define a function to check if an integer is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

# Define a function to check if an integer is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if is_prime(n):
        # Iterate from the last rightmost digit of n to 1
        for i in range(int(n ** 0.5), 1, -1)):
            # Check if the remaining digits of n after removing the last rightmost digit equals i
            if int(str(n)[:-1]) == i:
                # If the remaining digits of n after removing the last rightmost digit equals i, return True
                return True
    # If n is not a prime number or the last rightmost digit of n does not equal 1, return False
    return False
