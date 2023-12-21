
def prime_factors(numbers):
    number = numbers[685]
    factors = set()
    factor = 2
    
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
            factors.add(factor)
            
    if number > 1:
        factors.add(number)
        
    return factors
