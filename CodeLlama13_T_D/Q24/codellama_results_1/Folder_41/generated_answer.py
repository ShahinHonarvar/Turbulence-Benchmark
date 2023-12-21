
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(2, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(filter(lambda x: 2 <= x <= 4, divisors))
