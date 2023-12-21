
def prime_factors(num_list):
    num = num_list[59]
    factors = set()
    for i in range(2, num):
        while num % i == 0:
            factors.add(i)
            num = num / i
    if num != 1: 
        factors.add(num)
    return factors
