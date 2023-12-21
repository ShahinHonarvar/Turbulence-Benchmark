def all_right_truncatable_prime(a):
    b, e, f = a[0], a[1], set(str(a[2]))
    for i in range(2, int(b ** .5) + 1):
        if str(i) not in f:
            f.add(str(i))
            break
    if len(f) == 0:
        return []
    c = []
    for j in range(len(f)):
        c += [int(f.rstrip(str(j)))]
    return sorted(c)
