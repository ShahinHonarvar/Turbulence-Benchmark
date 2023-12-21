
def prime_factors(numbers):
    num = numbers[126]
    factors = set()
    
    i = 2
    while num > 1:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    return factors
