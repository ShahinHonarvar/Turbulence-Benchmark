
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list from index 29 to index 62 (both inclusive)
    for i in range(29, 63):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])
    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        # If it is, it is not a prime number
        return False

    # Check if any number between 2 and the square root of n is divisible by it
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # If it is divisible by any number between 2 and the square root of n, it is not a prime number
            return False

    # If none of the numbers between 2 and the square root of n are divisible by it, it is a prime number
    return True
