
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_indices = []
    for i in range(57, 65):
        if is_prime(lst[i]):
            prime_indices.append(lst[i])
    return sorted(prime_indices, reverse=True)
