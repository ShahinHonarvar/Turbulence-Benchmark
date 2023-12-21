
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    divisors_range = [d for d in divisors if 41 <= d <= 55]
    return sum(divisors_range) if divisors_range else 0
