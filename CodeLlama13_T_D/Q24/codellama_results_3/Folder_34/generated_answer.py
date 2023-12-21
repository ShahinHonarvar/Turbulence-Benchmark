
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum([x for x in divisors if 4 <= x <= 5]) or 0
