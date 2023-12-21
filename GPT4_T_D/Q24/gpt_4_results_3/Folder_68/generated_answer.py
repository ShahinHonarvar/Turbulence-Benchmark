
def sum_of_divisors_in_range(n):
    sum_divisors = 0
    if n > 2:
        for i in range(3, min(n+1, 7)):
            if n % i == 0:
                sum_divisors += i
    return sum_divisors
