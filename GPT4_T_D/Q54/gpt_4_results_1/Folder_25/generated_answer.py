
def all_right_truncatable_prime(tup):
    x = tup[92]
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        while n != 0:
            n //= 10
            if n != 0 and not is_prime(n):
                return False
        return True

    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(right_truncatable_primes)
