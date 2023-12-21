
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    return sum([d for d in divisors if 20 <= d <= 50])
