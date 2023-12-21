def find_divisors_in_range(n):
    # Your code here
    if n < 4:
        return []
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            yield i
    if n % 2 == 0:
        yield 2
    if n % 3 == 0:
        yield 3
    return
