
def all_right_truncatable_prime(n):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate through the numbers less than n
    for i in range(2, n+1):
        # Check if the number is prime
        if is_prime(i):
            # If it is prime, check if it is right-truncatable prime
            if is_right_truncatable_prime(i):
                # If it is right-truncatable prime, add it to the list
                prime_list.append(i)

    # Sort the list in descending order
    prime_list.sort(reverse=True)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return prime_list

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, n is prime
    return True

# Function to check if a number is right-truncatable prime
def is_right_truncatable_prime(n):
    # Check if n is prime
    if not is_prime(n):
        return False

    # Iterate from 10 to 99
    for i in range(10, 100):
        # If n is divisible by i, it is not right-truncatable prime
        if n % i == 0:
            return False

    # If we reach this point, n is right-truncatable prime
    return True
