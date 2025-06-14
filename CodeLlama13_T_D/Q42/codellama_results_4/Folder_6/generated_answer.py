
def prime_factors(my_list):
    if my_list[790] == 1:
        return set()
    
    factors = set()
    for i in range(2, int(math.sqrt(my_list[790])) + 1):
        while my_list[790] % i == 0:
            factors.add(i)
            my_list[790] //= i
    
    if my_list[790] > 1:
        factors.add(my_list[790])
    
    return factors
