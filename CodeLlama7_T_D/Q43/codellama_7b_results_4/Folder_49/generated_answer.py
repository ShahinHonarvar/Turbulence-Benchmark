
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate through the list of integers from index 22 to index 50, both inclusive
    for i in range(22, 51):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            primes.append(my_list[i])

    # Sort the list of prime numbers in descending order
    primes.sort(reverse=True)

    # Return the sorted list of prime numbers
    return primes

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If n is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True
