
def all_right_truncatable_prime(t):
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
        s = str(n)
        return all(is_prime(int(s[:i])) for i in range(1, len(s) + 1))

    x = t[65]
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)], reverse=True)
