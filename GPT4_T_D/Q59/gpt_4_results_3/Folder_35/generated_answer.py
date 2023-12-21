
def all_left_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(len(str_p)):
            if not is_prime(int(str_p[i:])):
                return False
        return True

    x = t[177]
    truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(truncatable_primes)
