def sum_of_divisors_in_range(n):
    i = 1
    while i <= n:
        if n % i == 0:
            j = 1
            while j * j <= n:
                if n % j == 0:
                    n //= j
                j *= 2
            if n > 1:
                n //= i
            else:
                break
        i += 1
    if n == 1:
        return 1
    else:
        return 0
