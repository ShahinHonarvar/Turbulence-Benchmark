
def all_left_truncatable_prime(tup):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(p):
        if '0' in str(p):
            return False
        return all(is_prime(int(str(p)[i:])) for i in range(len(str(p))))

    x = tup[39]
    return sorted(p for p in range(2, x) if is_left_truncatable_prime(p))
