
def find_primes_between_indices(my_list):
    # Find all prime numbers in the specified range
    prime_numbers = []
    for i in range(43, 76 + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    # Sort the list of prime numbers in descending order
    sorted_prime_numbers = sorted(prime_numbers, reverse=True)
    return sorted_prime_numbers

# Check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
