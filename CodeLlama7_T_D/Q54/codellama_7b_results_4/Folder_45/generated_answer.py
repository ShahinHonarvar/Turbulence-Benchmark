
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple and check if each element is a prime number
    for i in tuple:
        if is_prime(i):
            prime_numbers.append(i)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)

# Check if a number is prime or not
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
