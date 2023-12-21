def all_left_truncatable_prime(n):
    res = []
    for i in range(2, int(n[14]) + 1):
        if is_left_truncatable_prime(i):
            res.append(i)
    return res
def is_left_truncatable_prime(n):
    s = str(n)
    while s[0] != '':
        if s[0] == '0':
            return False
        elif s[0] not in '2357':
            return False
        s = s[1:]
    return True
