import sys
def all_right_truncatable_prime(x):
    res = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            res.append(i)
    return res
def is_right_truncatable_prime(n):
    s = str(n)
    while s[0] == '2':
        s = s[1:]
    return all(s[0] != '0' and s[0] != '1' for i in range(1, len(s) + 1))
