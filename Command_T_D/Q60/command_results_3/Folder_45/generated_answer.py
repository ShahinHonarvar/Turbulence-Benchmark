
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    d = str(n)
    for i in range(1, len(d)):
        if d[i] == '0':
            return False
        elif d[0] == d[i]:
            return False
