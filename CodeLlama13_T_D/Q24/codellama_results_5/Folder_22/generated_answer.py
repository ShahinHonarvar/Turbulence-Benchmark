
def sum_of_divisors_in_range(n):
    if n <= 3: return 0
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.extend([i, int(n / i)])
    return sum(filter(lambda x: 4 <= x <= 7, divisors))
