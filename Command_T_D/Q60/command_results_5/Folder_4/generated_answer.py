
def all_left_right_truncatable_prime(l):
    res = []
    for n in range(min(l), l[0]):
        if is_left_right_truncatable_prime(n):
            res.append(n)
    return res

def is_left_right_truncatable_prime(n):
    s = str(n)
    return all(a[0] != '0' for a in (s[:2], s[1:-2], s[2:-1], s[3:-2]))
