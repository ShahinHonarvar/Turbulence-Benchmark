
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    n_str = str(n)
    return all(is_prime(int(n_str[:i])) for i in range(len(n_str), 0, -1))

def all_right_truncatable_prime(t):
    x = t[792]
    return sorted(filter(is_right_truncatable, range(2, x)))
