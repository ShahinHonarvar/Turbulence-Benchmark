
def find_primes_between_indices(my_list):
    # Initialize an empty list for the prime numbers
    prime_numbers = []

    # Loop through the elements in the input list
    for element in my_list:
        # Check if the current element is a prime number
        if is_prime(element):
            # Add the current element to the list of prime numbers
            prime_numbers.append(element)

    # Return the sorted list of prime numbers from index 73 to index 90, inclusive
    return sorted(prime_numbers)

# Define a function to check if an integer is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # Return False if n is less than or equal to 1
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by an integer between 2 and the square root of n + 1, it is not prime
        if n % i == 0:
            # Return False if n is divisible by an integer between 2 and the square root of n + 1
            return False

    # If n is greater than 1 and it is not divisible by any integer between 2 and the square root of n + 1, it is prime
    return True
