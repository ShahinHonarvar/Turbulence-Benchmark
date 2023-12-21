
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate over the list of integers, starting from index 229
    for i in range(229, len(my_list)):

        # Check if the current number is prime
        if is_prime(my_list[i]):

            # If it is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime by iterating from 2 to the square root of the number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
