
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    indices = range(46, 62)
    primes = [n for i, n in enumerate(lst) if n in indices and is_prime(n)]
    return sorted(primes)
