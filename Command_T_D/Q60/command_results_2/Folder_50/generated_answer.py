
def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(tup[0], tup[1] + 1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(n):
    s = str(n)
    if s[0] == '0':
        return False
    if s[-1] == '0':
        return False
    for i in range(1, len(s)):
        if s[i] == '0':
            return False
    return True
