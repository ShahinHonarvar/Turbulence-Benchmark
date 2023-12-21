
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

    primes = [x for x in lst[59:98] if is_prime(x)]
    primes.sort(reverse=True)
    return primes
