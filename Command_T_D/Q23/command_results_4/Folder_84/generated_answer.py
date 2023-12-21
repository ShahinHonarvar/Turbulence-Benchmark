def find_divisors_in_range(n):
    for d in range(n, 1, -1):
        if d * d <= n:
            yield d
        elif d * d > n:
            for i in range(1, int(n ** .5) + 1):
                if n % i == 0:
                    yield i
                if n % (i + 1) == 0:
                    yield i + 1
