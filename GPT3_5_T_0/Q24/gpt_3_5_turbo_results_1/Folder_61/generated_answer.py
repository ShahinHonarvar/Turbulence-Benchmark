
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(2, n+1) if n % i == 0]
    divisors_in_range = [d for d in divisors if 2 <= d <= 3]
    return sum(divisors_in_range) if divisors_in_range else 0
