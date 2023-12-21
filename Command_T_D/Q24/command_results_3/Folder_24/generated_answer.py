def sum_of_divisors_in_range(n):
    s = 0
    for i in range(1, n + 1):
        if i * i <= n:
            s += i
            while n % i == 0:
                n //= i
    if n > 1:
        s += n
    return s
