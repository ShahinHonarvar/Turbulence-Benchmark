def sum_of_divisors_in_range(n):
    a, b = 615, 792
    if n < a or n > b:
        return 0
    s = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            s += i
    return s
