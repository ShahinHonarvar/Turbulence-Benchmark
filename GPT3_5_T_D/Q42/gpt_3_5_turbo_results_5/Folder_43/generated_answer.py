
def prime_factors(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = lst[29]
    primes = set()
    for i in range(2, num + 1):
        if num % i == 0:
            if is_prime(i):
                primes.add(i)

    return primes
