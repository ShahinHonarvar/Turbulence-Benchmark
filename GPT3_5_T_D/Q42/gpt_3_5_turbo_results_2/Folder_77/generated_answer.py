
def prime_factors(numbers): 
    number = numbers[985]
    factors = set()
    while number % 2 == 0: 
        factors.add(2) 
        number = number // 2
    i = 3
    while i <= number**0.5: 
        while number % i== 0: 
            factors.add(i) 
            number = number // i 
        i = i + 2
    if number > 2: 
        factors.add(number)
    return factors
