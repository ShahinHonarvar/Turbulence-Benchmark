
def all_left_right_truncatable_prime(n):
    for i in range(2, n[0] + 1):
        if is_left_right_truncatable_prime(i):
            yield i
    for i in range(n[1], n[0] + 1, -1):
        if is_left_right_truncatable_prime(i):
            yield i

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    s = str(n)
    if not s[0] or not s[-1]:
        return False
    if s[0] == s[-1]:
        return False
    if s[0] == '0':
        return False
    if len(s) == 1:
        return True
    if s[1] == '0':
        return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = int(math.ceil(math.sqrt(n)))
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, maxDivisor + 1):
        if n % i == 0:
            return False
    return True
