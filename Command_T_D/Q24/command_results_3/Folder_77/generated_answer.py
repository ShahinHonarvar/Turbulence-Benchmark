def sum_of_divisors_in_range(N):
    s = 0
    for i in range(111, 508):
        if N % i == 0:
            s += i
    return s
