import set
def prime_factors(a):
    s = set()
    for i in range(len(a)):
        if a[i] > 1:
            s.add(a[i])
            for j in range(a[i], 1, -1):
                if a[i] % j == 0:
                    s.add(j)
                    a[i] /= j
                    break
            if a[i] == 1:
                s.add(a[i])
    return s
