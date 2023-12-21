
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    sum_divisors = sum(divisors)
    return sum([d for d in divisors if 4 <= d <= 8]) if 4 <= sum_divisors <= 8 else 0
