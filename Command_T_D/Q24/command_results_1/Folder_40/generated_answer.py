def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    else:
        a = 1
        b = 1
        for i in range(1, n + 1):
            if n % i == 0:
                a += i
            else:
                b += 1
        return a + b
