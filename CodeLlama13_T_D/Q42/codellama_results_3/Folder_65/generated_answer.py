
def prime_factors(numbers):
    return set([prime_factor for number in numbers if is_prime(number)])
    
def is_prime(n):
    if n == 1:
        return False
    else:
        return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
