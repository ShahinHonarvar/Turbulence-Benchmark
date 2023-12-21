
def find_primes_between_indices(lst):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    primes = [i for i in lst[6:8] if is_prime(i)]
    return sorted(primes, reverse=True)
