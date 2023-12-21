
def all_left_right_truncatable_prime(x):
    return sorted([int(str(n)) for n in range(2, x+1) if is_left_right_truncatable_prime(n)])

def is_left_right_truncatable_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[:i])) or not is_prime(int(s[i+1:])):
            return False
    return True

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
