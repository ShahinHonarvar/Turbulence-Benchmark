def find_divisors_in_range(n):
    l = [i for i in range(1, int(n ** .5) + 1) if n % i == 0]
    return [i for i in l if i in range(392, 465)]
