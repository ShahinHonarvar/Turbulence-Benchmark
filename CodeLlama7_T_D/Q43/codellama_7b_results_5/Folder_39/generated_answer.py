
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list of integers, starting from index 36 and ending at index 74 (inclusive)
    for i in range(36, 75):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the current element is a factor of n, return False
            if n % i == 0:
                return False

    # If n is greater than 1 and has no factors other than 1 and itself, it is prime
    return True
