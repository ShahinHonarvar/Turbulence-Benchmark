def sum_of_divisors_in_range(n):
    l = 20
    r = 50
    if n <= l or n >= r:
        return 0
    s = 0
    while l < n:
        s += n / l
        l += 1
    while n > r:
        s += n / r
        n //= r
    return s
