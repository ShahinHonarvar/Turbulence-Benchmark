
def all_right_truncatable_prime(t):
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

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = t[41]
    right_truncatable_primes = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes, reverse=True)
