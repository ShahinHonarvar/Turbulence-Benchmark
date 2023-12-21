
def sum_of_divisors_in_range(n):
    if n < 1: return 0
    s = 0
    for i in range(6, 9 + 1):
        if n % i == 0 and i <= n:
            s += i
    return s
