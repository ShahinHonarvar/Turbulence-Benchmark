
def all_left_right_truncatable_prime(test_tup):
    res = []
    x = test_tup[0]
    for i in range(2, x // 2 + 1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(n):
    s = str(n)
    for i in range(1, len(s)):
        s = s[1:]
        if not s:
            return True
        if not is_prime(int(s)):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, 1 + int(n ** 0.5), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
