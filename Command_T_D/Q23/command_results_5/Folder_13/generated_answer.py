def find_divisors_in_range(N):
    l = list(range(472, 827))
    while len(l) > 1:
        m = l[len(l) // 2]
        if N % m == 0:
            l.append(m)
            l.remove(m)
            for i in range(m, N // m):
                l.append(i)
        else:
            l.remove(m)
    return l
