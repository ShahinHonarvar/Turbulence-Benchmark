
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[:-i or None])):
                return False
        return True

    x = t[42]
    return sorted(filter(is_right_truncatable, range(x)))
