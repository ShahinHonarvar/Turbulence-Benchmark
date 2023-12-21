
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    sum_val = 0
    for divisor in divisors:
        if 42 <= divisor <= 77:
            sum_val += divisor
    return sum_val
