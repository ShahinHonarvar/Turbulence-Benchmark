
def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    start_index = 238
    end_index = 636
    # Iterate through the list and check for prime numbers
    for i in range(start_index, end_index + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers, reverse=True)
# Check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
