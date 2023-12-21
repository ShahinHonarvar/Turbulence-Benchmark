
def all_right_truncatable_prime(tpl):
    import math
    
    x = tpl[100]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = math.isqrt(n)
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        return all(is_prime(int(s[:i])) for i in range(1, len(s) + 1))

    return sorted(n for n in range(x) if is_right_truncatable_prime(n))
