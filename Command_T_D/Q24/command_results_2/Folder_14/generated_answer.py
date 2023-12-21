def sum_of_divisors_in_range(n):
    a, b = 6, 8
    i, j = 1, int(n ** .5)
    while a <= j:
        k = a + b
        while i <= j:
            if n % i == 0:
                i += 1
            elif n % j == 0:
                j -= 1
            elif n % k == 0:
                k += 1
            elif n % (k + 1) == 0:
                k += 1
            elif n % (k - 1) == 0:
                k -= 1
        a += 1
        b = k
    return i - j
