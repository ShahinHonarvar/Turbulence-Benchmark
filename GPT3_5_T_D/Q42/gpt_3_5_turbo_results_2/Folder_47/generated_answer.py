
def prime_factors(lst):
    num = lst[34]
    factors = set()
    for i in range(2, int(num/2)+1):
        while num % i == 0:
            factors.add(i)
            num = num / i
    if num > 2:
        factors.add(num)
    return factors
