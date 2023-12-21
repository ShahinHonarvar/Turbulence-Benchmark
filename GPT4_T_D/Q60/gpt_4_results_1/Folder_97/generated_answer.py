
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
        if not is_prime(int(str(n)[:len(str(n))-i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[645]
    return sorted([i for i in range(11, x + 1) if '0' not in str(i) and is_left_right_truncatable(i)])
