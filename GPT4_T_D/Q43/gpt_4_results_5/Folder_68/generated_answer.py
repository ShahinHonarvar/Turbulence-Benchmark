
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

    primes = []
    for i in range(1, 6):
        if i < len(lst) and is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)
