
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = [i for i in lst[3:9] if is_prime(i)]
    primes.sort()
    return primes
