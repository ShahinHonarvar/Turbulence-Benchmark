def find_divisors_in_range(n):
    if n <= 19:
        return []
    for i in range(20, 70):
        if n % i == 0:
            yield i
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            yield i
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            yield i
