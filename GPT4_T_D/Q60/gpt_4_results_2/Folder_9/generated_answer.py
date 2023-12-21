
def all_left_right_truncatable_prime(n):
    import math
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = n[29]
    truncatable_primes = [i for i in range(x+1) if i > 10 and is_prime(i) and is_left_right_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)
