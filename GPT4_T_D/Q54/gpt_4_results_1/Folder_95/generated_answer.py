
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable(p):
        if p < 10:
            return True
        else:
            return is_prime(p) and is_right_truncatable(p // 10)

    x = t[77]
    primes = [i for i in range(x) if is_right_truncatable(i) and is_prime(i)]
    return sorted(primes)
