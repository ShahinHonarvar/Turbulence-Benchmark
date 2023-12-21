
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    primes = [x for x in lst[23:49] if is_prime(x)]
    return sorted(primes)
