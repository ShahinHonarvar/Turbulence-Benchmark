
def all_left_truncatable_prime(x):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through all numbers less than x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-truncatable prime
            if is_left_truncatable_prime(i):
                # If i is both a prime number and left-truncatable prime, add it to the list of prime numbers
                prime_list.append(i)
    # Return the sorted list of prime numbers found in the loop
    return sorted(prime_list, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than n
        for i in range(2, n + 1):
            # If the result of dividing n by i is not equal to 0, then i is not a factor of n and it is not prime
            if n % i == 0:
                return False

    # If the number is greater than 1 and it does not have any factors other than 1 and itself, then it is prime
    return True

# Define a function to check if a number is left-truncatable prime
def is_left_truncatable_prime(n):
    # Check if n is greater than 0
    if n > 0:
        # Loop through all numbers less than n
        for i in range(2, n + 1):
            # If the result of dividing n by i is not equal to 0, then i is not a factor of n and it is not left-truncatable prime
            if n % i == 0:
                return False

    # If the number is greater than 0 and it does not have any factors other than 1 and itself, then it is left-truncatable prime
    return True
