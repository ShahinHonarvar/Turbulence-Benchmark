
def find_primes_between_indices(int_list):
    from math import sqrt
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    primes = [n for n in int_list[112:362] if is_prime(n)]
    primes.sort(reverse=True)
    return primes
