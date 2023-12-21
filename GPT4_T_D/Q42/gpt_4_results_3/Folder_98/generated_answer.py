
def prime_factors(lst):
    num = lst[4]
    factors = []
    while num % 2 == 0:
        factors.append(2),
        num = num / 2
    for i in range(3,int(num**0.5)+1,2):
        while num % i== 0:
            factors.append(i),
            num = num / i
    if num > 2:
        factors.append(int(num))
    prime_factors = set(factors)
    return prime_factors
