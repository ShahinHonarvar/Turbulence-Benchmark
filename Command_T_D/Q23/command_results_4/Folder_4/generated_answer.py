def find_divisors_in_range(n):
    # Your code here
    if n < 48 or n > 60:
        return []
    for i in range(1, n // 2):
        if n % i == 0:
            yield i
    for i in range(1, n // 2):
        if n % i == 0:
            yield i
    for i in range(1, n // 2):
        if n % i == 0:
            yield i
