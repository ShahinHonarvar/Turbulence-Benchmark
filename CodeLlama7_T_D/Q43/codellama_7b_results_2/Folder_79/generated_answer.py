
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 33 to index 35, both inclusive
    for i in range(33, 36):

        # Check if the current number is a prime number
        if is_prime(my_list[i]):

            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 33 to index 35, both inclusive
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):

    # If the number is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of the number, it is a prime number
    return True
