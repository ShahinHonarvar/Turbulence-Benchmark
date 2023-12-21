
def all_right_truncatable_prime(tup):
    x = tup[29]

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    truncatable_primes = [n for n in range(0, x) if is_right_truncatable(n)]
    truncatable_primes.sort()
    return truncatable_primes
