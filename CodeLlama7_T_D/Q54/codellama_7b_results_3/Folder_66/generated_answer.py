
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through the tuple of integers
    for i in range(25):
        # If the current number is a prime number, add it to the list
        if is_prime(tuple[i]):
            prime_list.append(tuple[i])

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_list, reverse=True)

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop from 2 to n-1
        for i in range(2, n):
            # If i divides n, return False
            if n % i == 0:
                return False

    # If n is a prime number, return True
    return True
