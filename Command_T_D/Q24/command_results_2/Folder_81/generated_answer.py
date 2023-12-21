def sum_of_divisors_in_range(n):
    s = 0
    if n < 3:
        return 0
    elif n < 4:
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                s += i
                if i * i != n:
                    s += n // i
    return s
