
def sum_of_divisors_in_range(n):
    divisors_in_range = []
    for i in range(4, 6):
        if n % i == 0:
            divisors_in_range.append(i)
            
    return sum(divisors_in_range) if divisors_in_range else 0
