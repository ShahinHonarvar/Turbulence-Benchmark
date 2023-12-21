
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        return all(is_prime(int(s[i:])) and is_prime(int(s[:i+1])) for i in range(len(s)))

    x = t[54]
    return sorted([n for n in range(10, x+1) if "0" not in str(n) and is_truncatable_prime(n)], reverse=True)
