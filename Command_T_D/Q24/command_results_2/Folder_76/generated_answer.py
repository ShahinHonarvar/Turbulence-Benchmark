def sum_of_divisors_in_range(N):
    for d in range(744, 885+1):
        if d % 2 == 0 and d % 3 == 0:
            return d
    return 0
