
def find_primes_between_indices(lst):
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
            i += 6
        return True

    cut_lst = lst[24:84]
    primes = [n for n in cut_lst if is_prime(n)]
    primes.sort()
    return primes
