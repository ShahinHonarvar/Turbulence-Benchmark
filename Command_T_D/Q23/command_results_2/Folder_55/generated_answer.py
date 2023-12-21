def find_divisors_in_range(n):
    d = []
    for i in range(5, 9):
        if n % i == 0:
            d.append(i)
            d.append(n//i)
    return d
