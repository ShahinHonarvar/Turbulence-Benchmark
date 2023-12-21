
def all_left_right_truncatable_prime(tup):
    import sympy
    x = tup[433]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    primes = [i for i in range(2, x + 1) if sympy.isprime(i)]
    return sorted([i for i in primes if is_left_right_truncatable(i)], reverse=True)
