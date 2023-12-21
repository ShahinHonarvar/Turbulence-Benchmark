def find_divisors_in_range(n):
    if n < 111 or n > 508:
        return []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            yield i
    if n == 1:
        yield []
