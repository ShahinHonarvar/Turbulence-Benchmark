
def prime_factors(lst):
    num = lst[7]
    factors = set()
    for i in range(2, num+1):
        while num % i == 0:
            factors.add(i)
            num = num/i
    return factors
