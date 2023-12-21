
def all_left_right_truncatable_prime(num_tuple):
    import math

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = num_tuple[88]
    truncatable_primes = [n for n in range(x+1) if is_prime(n) and is_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)
