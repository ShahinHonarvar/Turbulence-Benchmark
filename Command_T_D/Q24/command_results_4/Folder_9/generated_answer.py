def sum_of_divisors_in_range(n):
    if n < 3 or n > 9:
        return 0
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            n //= i
            if n == 1:
                break
    return n
