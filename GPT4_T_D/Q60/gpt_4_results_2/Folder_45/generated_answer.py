
def all_left_right_truncatable_prime(numbers_tuple):
    import math
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True
    x = numbers_tuple[61]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(left_right_truncatable_primes)
