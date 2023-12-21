
def all_left_truncatable_prime(t):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def is_left_truncatable(p):
        p = str(p)
        if '0' in p: return False
        return all(is_prime(int(p[i:])) for i in range(len(p)))

    x = t[3]
    return sorted([i for i in range(x) if is_left_truncatable(i)], reverse=True)
