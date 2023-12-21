import itertools
def all_right_truncatable_prime(n):
    a, b = 2, n
    for d in itertools.permutations('234789', n):
        p = d + '0'
        if all(p[i] * 10**(n-i-1) > b for i in range(1, n+1)):
            yield from range(b+1, p[0]*10, -1)
            break
    if p[-1] * 10**(n-1) > b:
        yield from range(b+1, p[-1] * 10**(n-1), -1)
