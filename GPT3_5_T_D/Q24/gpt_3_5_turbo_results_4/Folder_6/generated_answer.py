
def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 58 <= i <= 90:
            divisors.append(i)
    return sum(divisors)
