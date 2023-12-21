
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, 8):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)
