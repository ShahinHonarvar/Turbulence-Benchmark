
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(x):
        while x:
            if is_prime(x):
                x //= 10
            else:
                return False
        return True

    x = t[792]
    return sorted([i for i in range(10, x) if is_right_truncatable(i)])
