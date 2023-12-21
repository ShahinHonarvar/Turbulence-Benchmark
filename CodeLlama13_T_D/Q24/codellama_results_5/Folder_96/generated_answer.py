
def sum_of_divisors_in_range(n):
    if n < 5:
        return 0
    
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    
    return sum(divisor for divisor in divisors if 5 <= divisor <= 9)
