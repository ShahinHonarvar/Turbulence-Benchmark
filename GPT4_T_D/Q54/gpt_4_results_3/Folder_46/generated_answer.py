
def all_right_truncatable_prime(t):
    import math
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = t[33]
    result = []
    for i in range(2, x):
        if is_right_truncatable(i):
            result.append(i)
    return sorted(result)
