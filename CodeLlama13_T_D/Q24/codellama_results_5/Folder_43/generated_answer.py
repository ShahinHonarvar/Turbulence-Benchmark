
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and 19 <= i <= 69:
            divisors.append(i)
    return sum(divisors) or 0
