
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    divisors_in_range = [d for d in divisors if 35 <= d <= 37]
    if divisors_in_range:
        return sum(divisors_in_range)
    else:
        return 0
