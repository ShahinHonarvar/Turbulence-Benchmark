def sum_of_divisors_in_range(n):
    if n < 113 or n > 991:
        return 0
    else:
        a = 1
        b = n
        c = 1
        d = 1
        while b != 0:
            c = (b + 1) // 2
            d = b // 2
            a += d
            b = c
            d = 1
            c = a + 1
            while c <= n:
                d = c // 2
                a += d
                c = d + 1
            return a
