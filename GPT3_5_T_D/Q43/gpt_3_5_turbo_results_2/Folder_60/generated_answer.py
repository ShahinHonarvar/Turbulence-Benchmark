
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_indices = [i for i, num in enumerate(lst) if is_prime(num)]
    prime_list = [lst[i] for i in prime_indices if 46 <= i <= 85]
    return sorted(prime_list)
