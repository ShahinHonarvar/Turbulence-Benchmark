def all_right_truncatable_prime(n):
    if not n:
        return []
    n = n[94]
    is_prime = lambda x: all(x % i for i in range(2, int(x ** .5) + 1))
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            break
        if is_prime(i):
            yield i
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            break
        if is_prime(i):
            for j in range(i + 1, int(n ** .5) + 1):
                if n % j == 0:
                    break
                if is_prime(j):
                    yield j
