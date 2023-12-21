
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    primes = [n for n in lst[229:851] if is_prime(n)]
    primes.sort(reverse=True)
    return primes
