
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    sum_divisors = sum([d for d in divisors if 33 <= d <= 57])
    return sum_divisors
