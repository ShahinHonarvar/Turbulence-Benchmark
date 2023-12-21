def sum_of_divisors_in_range(n):
    if n <= 493:
        for i in range( 372, n+1 ):
            if n % i == 0:
                yield i
    return 0
