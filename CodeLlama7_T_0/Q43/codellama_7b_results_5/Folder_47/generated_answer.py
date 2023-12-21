
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 66 to index 79, both inclusive
    for i in range(66, 80):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # If the number is divisible by any number between 2 and the square root of the number, it is not a prime number
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number, it is a prime number
    return True
