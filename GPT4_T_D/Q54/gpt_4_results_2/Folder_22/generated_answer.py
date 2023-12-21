
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        if is_prime(n):
            while n != 0:
                n //= 10
                if n > 0 and not is_prime(n):
                    return False
            return True
        else:
            return False

    x = t[85]
    return sorted([i for i in range(x) if right_truncatable_prime(i)])
