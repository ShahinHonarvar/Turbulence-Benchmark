
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the specified range of indices in the list
    for i in range(415, 647 + 1):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

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
