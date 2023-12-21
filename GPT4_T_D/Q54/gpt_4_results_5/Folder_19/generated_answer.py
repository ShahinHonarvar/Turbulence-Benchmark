
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5)
        for d in range(3, max_divisor + 1, 2):
            if n % d == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = t[67] if len(t) > 67 else 0
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes, reverse=True)
