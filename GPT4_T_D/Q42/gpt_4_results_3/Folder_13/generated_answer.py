
def prime_factors(lst):
    num = lst[126]
    
    fact_set = set()
    factor = 2
    while factor ** 2 <= num:
        if num % factor:
            factor += 1
        else:
            num //= factor
            fact_set.add(factor)
            
    if num > 1:
        fact_set.add(num)
        
    return fact_set
