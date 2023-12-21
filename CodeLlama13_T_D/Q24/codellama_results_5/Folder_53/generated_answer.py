
def sum_of_divisors_in_range(n):
    if n < 4 or n > 9:
        return 0
    
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i and n//i >= 4 and n//i <= 9:
                divisors.append(n//i)
    
    return sum(divisors)
