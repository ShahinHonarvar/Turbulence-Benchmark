
def find_primes_between_indices(my_list):
    # Initialize a new list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers, starting from index 546
    for i in range(546, len(my_list)):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 546 to index 941, both inclusive
    return sorted(prime_numbers, reverse=True)

# Define a function to check if an integer is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If any of the numbers from 2 to the square root of n divide n without leaving a remainder, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is divisible only by 1 and itself, it is prime
    return True
