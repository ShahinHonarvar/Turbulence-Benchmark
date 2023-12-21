
def sum_of_divisors_in_range(n):
    if n < 157 or n > 902:
        return 0
    
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    
    return sum(filter(lambda x: 157 <= x <= 902, divisors))
