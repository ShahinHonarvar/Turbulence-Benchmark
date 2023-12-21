
def all_left_right_truncatable_prime(n):
    x = n[92]
    res = []
    for a in range(2, x // 2 + 1):
        if all(str(a) in str(b) for b in range(a, x // 2 + 1, a)):
            res.append(a)
    for b in range(x // 2, x + 1):
        if all(str(b) in str(c) for c in range(b, x + 1, b)):
            res.append(b)
    return res
