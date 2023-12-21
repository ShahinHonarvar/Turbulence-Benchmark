
def all_left_right_truncatable_prime(t):
    x = t[55]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            left = s[:len(s) - i]
            right = s[i:]
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return True

    truncatables = [i for i in range(x + 1) if is_prime(i) and is_truncatable(i)]
    truncatables.sort()
    return truncatables
