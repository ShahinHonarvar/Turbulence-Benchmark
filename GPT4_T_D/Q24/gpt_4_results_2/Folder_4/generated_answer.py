
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(48, 61) if n % i == 0]
    sum_of_divisors = sum(divisors)
    
    return sum_of_divisors
