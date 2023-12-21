
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 10 to index 94, both inclusive
    for i in range(10, 95):

        # Check if the number at the current index is prime
        if is_prime(my_list[i]):
            # If it is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 10 to index 94, both inclusive. The returned list should be in descending order. If no prime number exists in the specified range, the function should return an empty list.
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        # If it is, return False
        return False

    # Check if any number between 2 and the square root of n is divisible by it
    for i in range(2, int(n ** 0.5) + 1):
        # If it is divisible, return False
        if n % i == 0:
            return False
