
def sum_of_divisors_in_range(n):
    if n <= 0: return 0
    divisors = []
    for i in range(1, 9):
        if n % i == 0 and i in range(1, 9):
            divisors.append(i)
    return sum(divisors) or 0
