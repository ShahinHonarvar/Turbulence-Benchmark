
def find_primes_between_indices(my_list):
    # Check if the input list is valid
    if not my_list or len(my_list) < 31 or len(my_list) > 95:
        return []

    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the input list and check for prime numbers
    for i in range(31, 96):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
