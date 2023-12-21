
def find_primes_between_indices(my_list):
    # Find the prime numbers in the specified range
    prime_numbers = []
    for i in range(3, 7):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)

def is_prime(n):

    # Check if 'n' is a prime number

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True
