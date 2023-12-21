def find_divisors_in_range(n):
    if n < 403 or n > 514:
        return []
    a = [i for i in range(1, int(n ** .5) + 1)]
    b = [i for i in range(2, n // 2 + 1)]
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] * b[j] <= n:
                c.append(a[i] * b[j])
    return c
