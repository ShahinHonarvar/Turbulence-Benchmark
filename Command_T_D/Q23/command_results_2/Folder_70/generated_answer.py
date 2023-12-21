def find_divisors_in_range(n):
    return [a for a in range(5**2,n//2+1,2) if n%a == 0]
