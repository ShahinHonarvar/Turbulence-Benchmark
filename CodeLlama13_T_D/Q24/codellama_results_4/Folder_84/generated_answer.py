
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(2, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum([d for d in divisors if 224 <= d <= 584])
