
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        return all(is_prime(int(s[:i+1])) and is_prime(int(s[i:])) for i in range(len(s)))

    x = t[77]
    return sorted([i for i in range(11, x+1) if is_truncatable(i)], reverse=True)
