def find_sum_of_multiples(n):
    a = 1
    b = n
    c = 0
    d = 1
    e = n * n
    while c < e:
        if d <= b:
            c += d
            d += n
        else:
            c += d
            d += n
            a += 1
            b += 1
            d = n * a
        if c > e:
            break
    return c
