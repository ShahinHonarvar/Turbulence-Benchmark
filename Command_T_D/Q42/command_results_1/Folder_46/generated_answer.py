import set
def prime_factors(a):
    s = set()
    s.add(a[453])
    for i in range(2, int(a[453]) + 1):
        if a[453] % i == 0:
            s.add(i)
            break
    return s
