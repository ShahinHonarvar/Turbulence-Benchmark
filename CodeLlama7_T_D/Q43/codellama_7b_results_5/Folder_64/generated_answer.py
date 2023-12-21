
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers starting from index 6
    for i in range(len(my_list)):
        if i < 6 or i > 6:
            continue

        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    return sorted(prime_numbers)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if the number is less than 2
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
