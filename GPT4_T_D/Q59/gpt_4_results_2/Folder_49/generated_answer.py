
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = round(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[14]
    return sorted([i for i in range(x) if is_left_truncatable_prime(i)])
