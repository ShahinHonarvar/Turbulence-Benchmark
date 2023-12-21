
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and 70 <= i <= 93:
            divisors.append(i)
    return sum(divisors)
