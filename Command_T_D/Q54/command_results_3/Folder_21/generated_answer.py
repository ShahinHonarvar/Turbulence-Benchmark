def all_right_truncatable_prime(x):
    s = str(x)
    n = len(s)
    a = [0] * n
    for i in range(n - 1):
        if s[i] == '9':
            break
        a[i + 1] = 10 ** i
    return sorted(list(filter(lambda x: x == x // 10**i * 10**(n - i) for i in range(n - 1))))
