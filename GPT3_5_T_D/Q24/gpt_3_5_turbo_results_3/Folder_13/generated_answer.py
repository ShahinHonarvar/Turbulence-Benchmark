
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and 472 <= i <= 827:
            divisors.append(i)
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)
