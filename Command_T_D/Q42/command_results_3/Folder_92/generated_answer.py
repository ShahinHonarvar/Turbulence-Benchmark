def prime_factors(a):
    l = []
    for x in range(2, a[0] // 2):
        if a[0] % x == 0:
            l.append(x)
            for y in range(x * 2, a[0] // 2, x):
                if a[0] % y == 0:
                    l.append(y)
                    for z in range(y * 2, a[0] // 2, y):
                        if a[0] % z == 0:
                            l.append(z)
                            break
    return set(l)
