
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum([d for d in divisors if 5 <= d <= 9]) or 0
