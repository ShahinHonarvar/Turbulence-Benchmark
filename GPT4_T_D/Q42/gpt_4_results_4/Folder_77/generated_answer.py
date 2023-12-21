
def prime_factors(lst):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        primes = set()
        for i in range(2, n + 1):
            if n % i == 0:
                if is_prime(i):
                    primes.add(i)
        return primes

    if len(lst) > 985:
        return factors(lst[985])
    else:
        return "List is too short"
