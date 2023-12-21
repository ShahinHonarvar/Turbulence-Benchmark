
def find_divisors_in_range(n):
    divisors_range = list(range(403, 515))
    divisors = [i for i in divisors_range if n % i == 0]
    
    return divisors
