
def find_primes_between_indices(my_list):
    # Find all prime numbers in the specified range
    prime_numbers = []
    for i in range(32, 59):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):

    # Check if 'n' is divisible by any number between 2 and the square root of 'n'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
