def all_left_truncatable_prime(n):
    l = []
    for i in range(2, n[0] + 1):
        if is_left_truncatable_prime(i):
            l.append(i)
    return sorted(l)
def is_left_truncatable_prime(n):
    c = str(n)
    if c[0] == '0':
        return False
    for i in range(1, len(c)):
        if c[i] == '0':
            return False
        elif c[i] not in '2357':
            return False
    return True
