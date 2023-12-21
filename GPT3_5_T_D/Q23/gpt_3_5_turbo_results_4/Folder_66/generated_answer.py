
def find_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return [x for x in divisors if 32 <= x <= 35]
