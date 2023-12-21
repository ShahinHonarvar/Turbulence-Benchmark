def sum_of_divisors_in_range(n):
    # your code here
    a = 1
    b = n // 2
    c = 1
    d = n // 2
    while b > 0:
        if b <= 50:
            a += b
            b -= 1
        elif b <= 84:
            c += b
            b += 1
        else:
            d += b
            b += 1
    return a + c + d
