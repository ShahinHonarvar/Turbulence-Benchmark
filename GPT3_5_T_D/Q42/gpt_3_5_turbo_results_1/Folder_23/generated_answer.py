
def prime_factors(integer_list):
    num = integer_list[69]
    factors = set()
    
    for i in range(2, num+1):
        while num % i == 0:
            factors.add(i)
            num = num / i
    
    return factors
