
def find_primes_between_indices(my_list):
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Iterate through the list from index 6 to index 7, both inclusive
    for i in range(len(my_list)-1):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If i divides n, return False
            if n % i == 0:
                return False

    # If n is a prime number, return True
    return True
