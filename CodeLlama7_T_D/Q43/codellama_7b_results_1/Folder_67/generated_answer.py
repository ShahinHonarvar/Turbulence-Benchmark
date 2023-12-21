
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through the indices of the list
    for i in range(18, 45):
        # Check if the current number is prime
        if is_prime(my_list[i]):
            # If it is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If it is, return False
        return False

    # Check if any number between 2 and the square root of n is divisible by it
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # If it is, return False
            return False

    # If none of the above conditions are met, return True
    return True
