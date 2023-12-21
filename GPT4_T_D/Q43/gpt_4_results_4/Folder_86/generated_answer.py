
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        p = 5
        while p * p <= n:
            if n % p == 0 or n % (p + 2) == 0:
                return False
            p += 6
        return True

    if len(lst) <= 781:
        return sorted([i for i in lst[459:] if is_prime(i)])

    return sorted([i for i in lst[459:782] if is_prime(i)])
