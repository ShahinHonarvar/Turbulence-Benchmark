
def all_right_truncatable_prime(tup):
    x = tup[65]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n:
            n //= 10
            if n and not is_prime(n):
                return False
        return True

    res = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    res.sort(reverse=True)
    return res
