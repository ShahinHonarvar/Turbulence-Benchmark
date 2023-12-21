def find_divisors_in_range(n):
    return [x for x in range(3, n//2+1) if n%x == 0]
