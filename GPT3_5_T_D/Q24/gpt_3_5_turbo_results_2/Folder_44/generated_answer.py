
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    sum_of_divisors = sum([d for d in divisors if 50 <= d <= 84])
    return sum_of_divisors if sum_of_divisors else 0
