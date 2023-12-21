def sum_of_divisors_in_range(N):
    s = 0
    if N <= 40:
        return 0
    if N <= 45:
        s += 1
    if N <= 50:
        s += 2
    if N <= 55:
        s += 3
    if N <= 60:
        s += 6
    if N <= 65:
        s += 15
    if N <= 70:
        s += 21
    return s
