
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()
    
    prime_factors = set()
    for number in numbers:
        if number <= 1:
            continue
        
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime_factors.add(i)
    
    return prime_factors
