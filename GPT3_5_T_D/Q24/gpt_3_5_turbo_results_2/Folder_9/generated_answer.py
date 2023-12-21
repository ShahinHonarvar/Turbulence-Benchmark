
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(3, n + 1):
        if n % i == 0:
            divisors.append(i)
    sum_divisors = sum(divisors)
    return sum_divisors if sum_divisors >= 3 and sum_divisors <= 9 else 0
