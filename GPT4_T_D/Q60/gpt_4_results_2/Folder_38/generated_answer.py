
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[i: len(str_n) - i])) for i in range(len(str_n))) and '0' not in str_n

    x = t[28]
    return sorted(filter(is_truncatable_prime, range(2, x + 1)))
