def sum_of_divisors_in_range(n):
    divisors = [i for i in range(3, n // 2 + 1) if n % i == 0]
    return sum(divisors) if len(divisors) > 0 else 0
