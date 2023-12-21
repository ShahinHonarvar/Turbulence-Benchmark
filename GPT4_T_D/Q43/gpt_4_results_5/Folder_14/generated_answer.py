
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for i, n in enumerate(lst) if 10 <= i <= 66 and is_prime(n)]
    primes.sort()
    return primes
