
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tup[29]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(right_truncatable_primes)
