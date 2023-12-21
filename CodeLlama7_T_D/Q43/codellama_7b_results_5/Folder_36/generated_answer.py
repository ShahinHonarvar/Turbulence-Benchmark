
def find_primes_between_indices(my_list):
    # Find the prime numbers in the specified range
    prime_numbers = []
    for i in range(167, 258):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    # Check if 'n' is divisible only by 1 and itself
    for i in range(2, n//2+1):
        if n % i == 0:
            return False

    return True
