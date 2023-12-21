
def find_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    range_divisors = [d for d in divisors if d >= 6 and d <= 7]
    return range_divisors
