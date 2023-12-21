def sum_of_divisors_in_range(n):
    s = set()
    for i in range(1, n + 1):
        if n % i == 0:
            s.add(i)
            if i * i != n:
                s.add(n // i)
    return sum(s)
