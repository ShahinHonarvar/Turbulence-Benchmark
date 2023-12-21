
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate through the list of integers starting from index 415
    for i in range(415, len(my_list)):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of primes
            primes.append(my_list[i])

    # Return the sorted list of prime numbers in ascending order
    return sorted(primes)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by any number between 2 and n-1, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n-1, it is prime
    return True
