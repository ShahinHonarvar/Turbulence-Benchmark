
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    sum_of_divisors = sum(divisors)
    result = sum([x for x in divisors if 3 <= x <= 8])
    return result if result != sum_of_divisors else 0
