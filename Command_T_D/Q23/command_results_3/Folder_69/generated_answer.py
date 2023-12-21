def find_divisors_in_range(n):
    l = []
    for x in range(658, 868+1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return l
