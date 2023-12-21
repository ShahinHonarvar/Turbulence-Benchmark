
def find_primes_between_indices(lst):
    prime_numbers = []
    for i in range(19, 72):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
