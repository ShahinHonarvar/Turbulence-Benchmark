
def prime_factors(numbers):
    num = numbers[24]
    if num < 2:
        return set()
    
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while (num % i) == 0:
            factors.add(i)
            num //= i
            if num < 2:
                break
    
    if num > 1:
        factors.add(num)
    
    return factors
