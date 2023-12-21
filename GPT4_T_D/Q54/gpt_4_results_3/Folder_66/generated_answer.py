
def all_right_truncatable_prime(t):
    x = t[25]
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        n = str(n)
        while len(n) > 1:
            n = n[:-1]
            if not is_prime(int(n)):
                return False
        return True

    rt_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(rt_primes, reverse=True)
