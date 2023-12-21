
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[41]
    return [n for n in range(x) if is_left_truncatable(n)]
