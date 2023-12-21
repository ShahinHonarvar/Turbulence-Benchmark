def find_divisors_in_range(n):
    l = [x for x in range(n+1) if n % x == 0]
    return [x for x in l if x in range(615, 792)]
