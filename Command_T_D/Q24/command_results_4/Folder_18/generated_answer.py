def sum_of_divisors_in_range(n):
    s = 0
    for i in range(387, 516):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
    return s
