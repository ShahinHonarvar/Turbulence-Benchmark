def find_divisors_in_range(n):
    if n < 35 or n > 98:
        return []
    for i in range(35, n//2):
        if n % i == 0:
            yield i
    for i in range(n//2, 98, 1):
        if n % i == 0:
            yield i
