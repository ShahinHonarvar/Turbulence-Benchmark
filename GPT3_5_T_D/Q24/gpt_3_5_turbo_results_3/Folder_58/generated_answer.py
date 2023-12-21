
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0 and 403 <= i <= 514]
    return sum(divisors) if len(divisors) > 0 else 0
