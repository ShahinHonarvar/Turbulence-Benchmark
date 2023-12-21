
def prime_factors(lst):
    num = lst[37]
    factors = set()
    for i in range(2, num+1):
        while num % i == 0:
            num /= i
            factors.add(i)
        if num == 1:
            break            
    return factors
